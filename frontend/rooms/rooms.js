$(document).ready(function() {
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
        // You can send the roomName to your backend (Go) to save in the database
        // Assuming you have a function to add the room to the database
        // Example: addRoomToDatabase(roomName);
        
        // For now, let's just add it to the list
        addRoomToList(roomName);
        $("#roomName").val(""); // Clear the input field
    });
});