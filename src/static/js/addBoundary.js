
/**
 * @description Function to add a new variable to the form
 * @param {event} event - The event that triggered the function
 * @return {void}
 */
function addBoundary(event) {
    "use strict";
    event.preventDefault();
    // Get the current number of variables
    let variablesSection = document.getElementById('variables');
    let numVariables = variablesSection.children.length;
    // Create new boundary div
    let newBoundaryDiv = document.createElement('div');
    newBoundaryDiv.className = `boundary ${numVariables}-boundary `;
    // style the boundary div
    newBoundaryDiv.style.display = 'flex';
    newBoundaryDiv.style.flexDirection = 'row';
    newBoundaryDiv.style.justifyContent = 'space-between';

    // Create new container for lower, variable, and upper
    let lowerDiv = document.createElement('div');
    let variableDiv = document.createElement('div');
    let upperDiv = document.createElement('div');
    // Style the new divs
    lowerDiv.style.display = 'flex';
    lowerDiv.style.flexDirection = 'column';
    lowerDiv.style.justifyContent = 'space-between';
    variableDiv.style.display = 'flex';
    variableDiv.style.flexDirection = 'column';
    variableDiv.style.justifyContent = 'space-between';
    upperDiv.style.display = 'flex';
    upperDiv.style.flexDirection = 'column';
    upperDiv.style.justifyContent = 'space-between';

    // Add class names to the divs
    lowerDiv.className = `lower lower-${numVariables}`;
    variableDiv.className = `variable variable-${numVariables}`;
    upperDiv.className = `upper upper-${numVariables}`;

    // Add the oninput to divs
    lowerDiv.oninput = function(event) { updateLabelsLowerLabel(event); };
    variableDiv.oninput = function(event) { updateLabelsVariableLabel(event); };
    upperDiv.oninput = function(event) { updateLabelsUpperLabel(event); };

    // Lower label
    let lowerLabel = document.createElement('label');
    lowerLabel.for = `lower-${numVariables}`;
    lowerLabel.innerHTML = 'Lower';
    lowerLabel.id = `lower-label-${numVariables}`
    // Append the label to the lower div
    lowerDiv.appendChild(lowerLabel);
    // Create input for lower bound
    let lowerInput = document.createElement('input');
    lowerInput.type = 'text';
    lowerInput.name = `lower-${numVariables}`;
    lowerInput.id = `lower-${numVariables}`;
    lowerInput.placeholder = 'Enter the lower bound';
    // Append the input to the lower div
    lowerDiv.appendChild(lowerInput);
    // Append the lower div to the new boundary div
    newBoundaryDiv.appendChild(lowerDiv);

    // Variable label
    let variableLabel = document.createElement('label');
    variableLabel.for = `variable-${numVariables}`;
    variableLabel.innerHTML = 'variable';
    variableLabel.id = `variable-label-${numVariables}`;
    variableDiv.appendChild(variableLabel);

    // Create input for variable
    let variableInput = document.createElement('input');
    variableInput.type = 'text';
    variableInput.name = `variable-${numVariables}`;
    variableInput.id = `variable-${numVariables}`;
    variableInput.placeholder = 'Enter the variable';
    variableDiv.appendChild(variableInput);
    newBoundaryDiv.appendChild(variableDiv);

    // Upper label
    let upperLabel = document.createElement('label');
    upperLabel.for = `upper-${numVariables}`;
    upperLabel.innerHTML = 'Upper';
    upperLabel.id = `upper-label-${numVariables}`;
    upperDiv.appendChild(upperLabel);

    // Create input for upper bound
    let upperInput = document.createElement('input');
    upperInput.type = 'text';
    upperInput.name = `upper-${numVariables}`;
    upperInput.id = `upper-${numVariables}`;
    upperInput.placeholder = 'Enter the upper bound';
    upperDiv.appendChild(upperInput);
    newBoundaryDiv.appendChild(upperDiv);

    // Append the new variable div below the last variable div
    variablesSection.appendChild(newBoundaryDiv);
}
