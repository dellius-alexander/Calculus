
/**
 * @description Remove variable boundary from the map
 * @param {Event} event
 * @return {void}
 */
function removeBoundary(event) {
    "use strict";
    event.preventDefault();
    // Remove the last element in the variable boundary div list
    let boundaryDiv = document.getElementById("variables");
    boundaryDiv.removeChild(boundaryDiv.lastElementChild);
}
