async function submitForm(event) {
    event.preventDefault();

    const form = document.getElementById('user-form');
    const formData = new FormData(form);
    const jsonData = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/api/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': form.querySelector('input[name="csrf_token"]').value, //manually define POST method, and add content type and csrf token to header
            },
            body: JSON.stringify(jsonData),
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error('Error response:', errorText);
            alert(`Error: ${errorText}`);
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
