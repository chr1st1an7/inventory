$(document).ready(function() {
    const apiUrl = "http://127.0.0.1:5000/api/room";

    // Function to make a GET request to the API
    function requestDatafromAPI(apiUrl) {
        return fetch(apiUrl)
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`Request failed with status: ${response.status}`);
                }
                return response.json(); // Parse the response body as JSON
            });
    }

    // Function to send data to the API
    function sendDatatoAPI(apiUrl, roomData) {
        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(roomData)
        })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Request failed with status: ${response.status}`);
            }
            // Handle success if needed
            console.log('Data sent successfully:', roomData);
        })
        .catch((error) => {
            console.error('Request error:', error);
        });
    }

    // Function to add a room to the list
    function addRoomToList(roomName) {
        const roomList = document.getElementById("roomList");
        const listItem = document.createElement("li");
        const anchor = document.createElement("a");

        // Set the href attribute to link to the individual room page
        anchor.href = `/${roomName.toLowerCase().replace(/\s+/g, '-')}`;
        anchor.textContent = roomName;

        listItem.appendChild(anchor);
        roomList.appendChild(listItem);
    }

    // Handle form submission
    $("#addRoomForm").submit(function(event) {
        event.preventDefault();
        const roomName = $("#roomName").val();

        // Create room data object
        const roomData = {
            room_name: roomName,
            categories: "[]" // Add categories if needed
        };

        // Send data to the API
        sendDatatoAPI(apiUrl, roomData);

        // Add the room to the list
        addRoomToList(roomName);

        $("#roomName").val(""); // Clear the input field
    });

    // Request data from the API and add rooms to the list
    requestDatafromAPI(apiUrl)
        .then((data) => {
            const rooms = data.rooms;
            rooms.forEach((roomData) => {
                const [roomId, roomName, categoriesString] = roomData;
                const categories = JSON.parse(categoriesString.replace(/'/g, '"'));
                const formattedRoomName = roomName
                addRoomToList(formattedRoomName);
            });
        })
        .catch((error) => {
            console.error('Request error:', error);
        });
});
