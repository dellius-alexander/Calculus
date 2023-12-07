import time
import traceback
from typing import Tuple, List, Union, Optional
import re
import yaml
from sympy import symbols, pprint, cos, pi, sqrt, exp, init_printing, solve, sin, atan, tan, Function, \
    latex, sympify, oo
from integral import MultipleIntegral
from fastapi import FastAPI, Request, Depends, HTTPException, Form, Body
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
from myLogger.logger import get_logger

i, j, k, x, y, z, x0, y0, z0, a, b, c, d, dx, t, r, dr, dy, dz, rho, theta, phi = \
    symbols("i, j, k, x, y, z, x0, y0, z0, a, b, c, d, dx, t, r, dr, dy, dz, rho, theta, phi")

init_printing(latex_mode="inline")

logger = get_logger(__name__)

###############################################################################
app = FastAPI()

# Add middleware
app.add_middleware(
    CORSMiddleware,
    # Remember to replace allow_origins=["*"] with your actual client's origin
    # in production to prevent Cross-Site Request Forgery (CSRF) attacks.
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")
###############################################################################
# Init timestamp
###############################################################################
start_time = time.time_ns()


###############################################################################


def get_uptime() -> float:
    return time.time_ns() - start_time


###############################################################################
# Configuration
###############################################################################


def load_config(config_path):
    with open(config_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logger.debug(exc)


###############################################################################


def get_function_property(x, function, form: Form):
    try:
        function_regex = re.compile(r"^(function(s)?)-?\d*$", re.IGNORECASE)
        for key, value in form.items():
            match_function = function_regex.search(key)
            if match_function and x in "functions":
                cleaned = value.replace("^", "**")
                return [function(cleaned)]
        return None
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()
        return None


def count_variables(form: Form):
    try:
        variable_regex = re.compile(r"^(variable(s)?)-?\d*$", re.IGNORECASE)
        variable_count = 0
        for key in form.keys():
            if variable_regex.search(key):
                variable_count += 1
        return variable_count
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()
        return None


def get_interval_property(x, form: Form):
    try:
        interval_regex = re.compile(r"^(lower|upper)-\d*$", re.IGNORECASE)
        properties = []
        interval_sentinel = 0
        variable_count = count_variables(form=form)
        for key, value in form.items():
            match_interval = interval_regex.search(key)
            if match_interval and x in "intervals" and interval_sentinel < variable_count:
                try:
                    lower_value = form.get(f"lower-{interval_sentinel}").replace("^", "**")
                    upper_value = form.get(f"upper-{interval_sentinel}").replace("^", "**")
                    lower_value = sympify(lower_value) if lower_value is not None else -oo
                    upper_value = sympify(upper_value) if upper_value is not None else oo
                    properties.append((lower_value, upper_value))

                except TypeError:
                    logger.debug(f"Missing upper or lower value for interval {interval_sentinel}")
                interval_sentinel += 1
        return properties if len(properties) >= 1 else None
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()
        return None


def get_variable_property(x, function, form: Form):
    try:
        variable_regex = re.compile(r"^(variable(s)?)-?\d*$", re.IGNORECASE)
        properties = []
        for key, value in form.items():
            match_variable = variable_regex.search(key)
            if match_variable and x in "variables":
                properties.append(function(value))
        return properties if len(properties) >= 1 else None
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()
        return None


def get_system_property(x, function, form: Form):
    try:
        system_regex = re.compile(fr"^({x})$", re.IGNORECASE)
        for key, value in form.items():
            match_system = system_regex.search(key)
            if match_system:
                return [function(value)]
        return None
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()
        return None


def get_property_from_form(x, function, form: Form):
    properties = []
    property_type_to_function = {
        "function": get_function_property,
        "intervals": get_interval_property,
        "variable": get_variable_property,
        "system": get_system_property
    }
    try:
        # Check if form is a dictionary or an object
        if not isinstance(form, dict):
            raise TypeError("Input should be a valid dictionary or object to extract fields from")

        for property_type, extraction_function in property_type_to_function.items():
            if property_type == "intervals":
                property_value = extraction_function(x, form)
                if property_value is not None:
                    properties.extend(property_value)
            else:
                property_value = extraction_function(x, function, form)
                if property_value is not None:
                    properties.extend(property_value)
        return properties if len(properties) >= 1 else None
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()
        raise e


def main(func: Function, var: Union[List, Tuple], intervals: Union[List, Tuple], system: str):
    """

    Args:
        func: the function to be integrated
        var: the variables of integration, i.e. [x, y, z] or [E_0, E_1, E_2,..., E_n]
        intervals: the intervals of integration, in the order of the variables of integration
        system: the coordinate system to be used. Options are cartesian, spherical, cylindrical, and polar
    Returns: the solution to the integral
    """
    try:
        logger.debug(f"""\n
        function: {func}\n
        variables: {var}\n
        intervals: {intervals}\n
        system: {system}
        """)
        # check the function parameters before proceeding
        if func is None:
            raise ValueError("func cannot be None")
        if var is None or not isinstance(var, (list, tuple)):
            raise TypeError("var must be a list or a tuple")
        if intervals is None or not isinstance(intervals, (list, tuple)):
            raise TypeError("intervals must be a list or a tuple")
        spherical_regex = re.compile(r"^(spherical|sph)$", re.IGNORECASE)
        cylindrical_regex = re.compile(r"^(cylindrical|cyl)$", re.IGNORECASE)
        polar_regex = re.compile(r"^(polar|pol)$", re.IGNORECASE)
        cartesian_regex = re.compile(r"^(cartesian|cart)$", re.IGNORECASE)
        if cartesian_regex.match(system):
            logger.debug(f"""
            Cartesian coordinates:
            func: {func}
            variables: {var}
            intervals: {intervals}
            """)
            return MultipleIntegral(func=func, variables=var, intervals=intervals)
        elif spherical_regex.match(system):
            logger.debug(f"""
            Spherical coordinates:
            func: {func}
            variables: {var}
            intervals: {intervals}
            """)
            return MultipleIntegral.solve_sphere(func=func, variables=var, intervals=intervals)
        elif cylindrical_regex.match(system):
            logger.debug(f"""
            Cylindrical coordinates:
            func: {func}
            variables: {var}
            intervals: {intervals}
            """)
            return MultipleIntegral.solve_cylindrical(func=func, variables=var, intervals=intervals)
        elif polar_regex.match(system):
            logger.debug(f"""
            Polar coordinates:
            func: {func}
            variables: {var}
            intervals: {intervals}
            """)
            return MultipleIntegral.solve_polar(func=func, intervals=intervals)
        else:
            raise ValueError("func must be in cartesian or spherical coordinates")

    except Exception as e:
        logger.debug(e)
        traceback.print_exc()
        return None


###############################################################################
# Routes
###############################################################################
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    try:
        if request.method == "GET":
            return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()
        return RedirectResponse(url="/")


@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    try:
        if request.method == "GET":
            return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()
        return RedirectResponse(url="/")


class FormData(BaseModel):
    function: str | None
    variables: list | tuple | dict | None
    intervals: list | tuple | dict | None
    system: str | None


@app.api_route(
    name="submit",
    path="/submit",
    methods=["GET", "POST"],  # Add "PUT" here
    response_class=HTMLResponse,
    response_model=FormData,)
async def api_submit(request: Request) -> HTMLResponse or RedirectResponse:
    try:
        form_data = None
        # Try to get the Form data
        try:
            form_data = await request.form()
        except Exception as e:
            raise ValueError("Invalid input:\n" + e)

        # Convert the form data to a dictionary
        form = dict(form_data)

        logger.debug("Processing the form...")
        logger.debug(f"Request method: {request.method}")
        logger.debug(f"Request payload: {form}")
        logger.debug(f"Request items: {[a for a in request.items()]}")

        properties = {
            "function": get_property_from_form("function", sympify, form)[0],
            "variables": get_property_from_form("variables", symbols, form),
            "intervals": get_property_from_form("intervals", None, form),
            "system": get_property_from_form("system", str, form)[0],
        }
        logger.info(f"Properties: \n{properties}")
        if request.method == "POST" \
                and properties["function"] is not None \
                and len(properties["variables"]) >= 1 \
                and len(properties["intervals"]) >= 1 \
                and properties["system"] is not None:

            logger.info("Processing the form...")

            iterated_integral = main(
                func=properties["function"],
                var=properties["variables"],
                intervals=properties["intervals"],
                system=properties["system"])

            logger.info("Finished integrating ......")
            # logger.info(iterated_integral)
            logger.info(f"""
            function: {iterated_integral.functions}
            variables: {iterated_integral.variables}
            intervals: {iterated_integral.intervals}
            system: {properties["system"]}
            integrals: {iterated_integral.integrals}
            anti-derivatives: {iterated_integral.anti_derivatives}
            results: {iterated_integral.results}
            """)
            return templates.TemplateResponse(
                name="results.html",
                context={
                    "request": request,
                    "function": latex(eval(str(iterated_integral.functions[-1]))),
                    "variables": latex(iterated_integral.variables),
                    "intervals": latex(iterated_integral.intervals),
                    "integrals": latex(iterated_integral.integrals[-1]),
                    "system": properties["system"],
                    "results": latex(iterated_integral.results[-1]),
                })

        else:
            raise ValueError("Invalid input:\n" + str(request.form))
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()
        return RedirectResponse(url="/")


@app.api_route(
    name="healthcheck",
    path="/healthcheck",
    methods=["GET", "POST"])
async def healthcheck(request: Request) -> JSONResponse or None:
    try:
        # Get the form data
        # Try to get the JSON payload
        try:
            payload = await request.json()
        except Exception as e:
            logger.error(f"""
            Failed to parse JSON payload: {e}
            Request payload: {request.body}
            Request items: {[a for a in request.items()]}
            No json payload found.""")
            payload = None

        logger.debug(f"""
        Healthcheck completed. Check the console for details.
        Request method: {request.method}
        Request payload: {payload}
        Request items: {[a for a in request.items()]}
        """)

        # now return the json payload to the client with the service uptime.
        return {
            "status": "success",
            "message": "Healthcheck completed. Check the console for details.",
            "uptime": "{:.2f} Minutes".format(get_uptime() / 1e9 / 60)
        }
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()
        return None


if __name__ == "__main__":
    ######################################################################
    config = load_config('resources/config.yaml')
    logger.debug(f"Configuration: \n{config}")
    uvicorn.run(
        app="src.__main__:app",
        host=config['server']['host'],
        port=config['server']['port'],
        http="auto",
        root_path="/",
        reload=True,  # reload the server when code changes
    )
    ######################################################################
