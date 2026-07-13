// Handles updating a task's status from the dropdown on the board
// without needing a full page reload.

function getCookie(name) {
    // grabs the CSRF token cookie Django sets - needed for the POST below
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function updateTaskStatus(taskId, newStatus) {
    fetch(`/task/${taskId}/status/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: `status=${newStatus}`,
    })
    .then(response => response.json())
    .then(data => {
        if (data.ok) {
            // simplest way to reflect the move without writing drag-drop logic
            window.location.reload();
        } else {
            alert('Could not update task status.');
        }
    })
    .catch(() => alert('Something went wrong updating the task.'));
}
