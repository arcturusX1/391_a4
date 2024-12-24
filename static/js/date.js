document.addEventListener("DOMContentLoaded", ()=>{
    async function check_dates() {
        const mechanic_id = document.getElementById('mechanic-id').textContent
        try{
            const response = await fetch(`/api/appointment/${mechanic_id}`)

            if (!response.ok){
                throw new Error(`error:${response.status}`)
            }

            const mechanic_data = await response.json()
            console.log(mechanic_data)
        }
        catch(error){
            throw new Error(`error: ${error}`)
        }
        
    }
    function flatpickr_instance(){
        const datePicker = document.getElementById("date-picker")
        const fp_instance = flatpickr(
            datePicker, {
                dateFormat: "Y-m-d",
                enableTime: true,
                altInput: true,
                altFormat: "F J, Y h:i k"
            }
        )

        return fp_instance
    }

    flatpickr_instance()
    check_dates()
}
)