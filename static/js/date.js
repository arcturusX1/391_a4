document.addEventListener("DOMContentLoaded", ()=>{
    async function check_dates() {
        try{
            fetch
        }
        
    }
    function flatpickr_instance(){
        const datePicker = document.getElementById("date-picker")

        const fp_instance = flatpickr(
            datePicker, {
                enableTime: true,
                altInput: true,
                altFormat: "F J, Y h:i k"
            }
        )

        return fp_instance
    }

    flatpickr_instance()
}
)