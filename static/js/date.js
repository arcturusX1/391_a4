document.addEventListener("DOMContentLoaded", () => {
    async function check_dates() {
        const mechanic_id = document.getElementById('mechanic-id').textContent;
        try {
            const response = await fetch(`/api/appointment/${mechanic_id}`);

            if (!response.ok) {
                throw new Error(`error: ${response.status}`);
            }

            const mechanic_data = await response.json();
            console.log(mechanic_data);

            // Convert booked dates to JavaScript Date objects
            const bookedDates = mechanic_data.dates.map(date => {
                const [year, month, day, hour, minute] = date.split('-');
                return new Date(year, month - 1, day, hour, minute); // JavaScript Date object
            });

            // Reinitialize Flatpickr with disabled dates
            flatpickr_instance(bookedDates);
        } catch (error) {
            console.error(`Error fetching dates: ${error}`);
        }
    }

    function flatpickr_instance(disabledDates = []) {
        const datePicker = document.getElementById("date-picker");
        flatpickr(datePicker, {
            dateFormat: "Y-m-d",
            enableTime: true,
            altInput: true,
            altFormat: "F J, Y h:i K", // User-friendly format
            disable: disabledDates, // Disable the provided dates
        });
    }

    // Initialize Flatpickr and fetch dates
    check_dates();
});
