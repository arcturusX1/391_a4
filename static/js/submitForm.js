async function submitForm(event) {
    event.preventDefault();

    const form = document.getElementById('user-form');
    const formData = new FormData(form); //FormData takes data from a form
    const jsonData = Object.fromEntries(formData.entries()); //convert form data to json
    const mechanic_id = document.getElementById('mechanic-id').textContent
    jsonData.mechanic_id = mechanic_id

    try {
        const response = await fetch('/api/appointment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': form.querySelector('input[name="csrf_token"]').value,
                //manually define POST method, and add content type and csrf token to header
            },
            body: JSON.stringify(jsonData),
        });

        if (!response.ok) {       
            const errorData = await response.json();
            // Display field-specific errors
            console.log(errorData)
            if (errorData.errors) {
                Object.entries(errorData.errors).forEach(([field, messages]) => {
                    const errorSpan = document.getElementById(`${field}_error`); //target span id
                    if (errorSpan) {
                        errorSpan.textContent = messages.join(', ');
                    }
                });
            }
            return;
        }

        const result = await response.json();
        alert('User added successfully!');
        console.log(result);
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred.');
    }
}
