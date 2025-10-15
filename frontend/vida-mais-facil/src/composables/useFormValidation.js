export function useFormValidation(callback) {
    function validateForm(event) {
        const formElement = event.target

        if (!formElement.checkValidity()) {
            formElement.classList.add('was-validated')
            return
        }

        formElement.classList.remove('was-validated')
        callback(event)
    }

    return {
        validateForm
    }
}