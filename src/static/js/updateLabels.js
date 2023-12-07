"use strict";
    /**
     * @description Update the function label to match the function input
     * @return {void}
     */
    function updateLabelsFunctionLabel() {
        // Get the function label
        let functionLabel = document.getElementById('function-label');
        // Get the function input
        let functionInput = document.getElementById('function');
        // Update the function label
        functionLabel.innerHTML = functionInput.value;
        // check if the label and input match and if not, update the label again
        if (functionLabel.innerHTML !== functionInput.value) {
            updateLabelsFunctionLabel();
        } else if (functionLabel.innerHTML === '') {
            functionLabel.innerHTML = 'Function';
        }
    }
    /**
     * @description Update the lower label to match the lower input
     * @param {Event} event - The event that triggered the function
     * @return {void}
     */
    function updateLabelsLowerLabel(event) {
        // Get the lower input inside the calling element
        let lowerInput = document.getElementById(event.target.id);
        // get the lower label inside the calling element
        let lowerLabel = lowerInput.previousElementSibling;
        // Update the lower label
        lowerLabel.innerHTML = lowerInput.value;
        // check if the label and input match and if not, update the label again
        if (lowerLabel.innerHTML !== lowerInput.value) {
            updateLabelsLowerLabel(event);
        } else if (lowerLabel.innerHTML === '') {
            lowerLabel.innerHTML = 'Lower';
        }
    }

    /**
     * @description Update the variable labels to match the variable inputs
     * @param {Event} event - The event that triggered the function
     * @return {void}
     */
    function updateLabelsVariableLabel(event) {
        // Get the variable input inside the calling element
        let variableInput = document.getElementById(event.target.id);
        // get the variable label inside the calling element
        let variableLabel = variableInput.previousElementSibling;
        // Update the variable label
        variableLabel.innerHTML = variableInput.value;
        // check if the label and input match and if not, update the label again
        if (variableLabel.innerHTML !== variableInput.value) {
            updateLabelsVariableLabel(event);
        } else if (variableLabel.innerHTML === '') {
            variableLabel.innerHTML = 'Variable';
        }
    }

    /**
     * @description Update the upper label to match the upper input
     * @param {Event} event - The event that triggered the function
     * @return {void}
     */
   function updateLabelsUpperLabel(event) {
        // Get the upper input inside the calling element
        let upperInput = document.getElementById(event.target.id);
        // get the upper label inside the calling element
        let upperLabel = upperInput.previousElementSibling;
        // Update the upper label
        upperLabel.innerHTML = upperInput.value;
        // check if the label and input match and if not, update the label again
        if (upperLabel.innerHTML !== upperInput.value) {
            updateLabelsUpperLabel(event);
        } else if (upperLabel.innerHTML === '') {
            upperLabel.innerHTML = 'Upper';
        }
    }
