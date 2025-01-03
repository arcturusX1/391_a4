async function fetchMechanics(){
    try{
        const response = await fetch('/api/mechanics')
        
        if(!response.ok){
            throw new Error(`error: ${response.status}`)
        }

        const data = await response.json();
        return data
    }
    catch(error){
        throw Error(`error: ${error}`)
    }
}


function showMechanics(data){
    const table = document.getElementById("mechanicTable").querySelector('tbody')
    data.forEach(item => {
        console.log(`row for ${item.id}`)
        const row = document.createElement('tr') //row

        const idCell = document.createElement('td') //cell
        idCell.textContent = item.id
        row.appendChild(idCell)

        const nameCell = document.createElement('td') //cell
        nameCell.textContent = item.name
        row.appendChild(nameCell)

        if (item.appt_number < 4) {
            const bookCell = document.createElement('td')
            const bookButton = document.createElement('button')
            bookButton.textContent = 'Book'
            bookCell.appendChild(bookButton)
            row.appendChild(bookCell)
            const current_id = item.id
            console.log(`EL for ${item.id}`)
            bookButton.addEventListener('click', () => handleClick(current_id)) //redirect to user form. arrow function so that it doesn't get triggered immediately. 
        }
        else {
            const bookCell = document.createElement('td')
            bookCell.textContent = 'Booked'
            row.appendChild(bookCell)
        }

        table.appendChild(row)

    })
}

async function getMechanics() {
    try{
    const mechanic_data = await fetchMechanics()
    showMechanics(mechanic_data)
    }
    catch(error){
        throw Error(`error: ${error}`)
    }
}

function handleClick(id){
    const path = `/book_mechanic/${id}`
    window.location.href = path
}

getMechanics();
