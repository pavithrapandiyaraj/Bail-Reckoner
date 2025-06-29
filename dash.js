document.addEventListener('DOMContentLoaded', function() {
    // Placeholder data for ongoing cases and notifications
    const ongoingCases = [
        { caseNumber: '12345', caseTitle: 'State vs John Doe', status: 'Pending' },
        { caseNumber: '67890', caseTitle: 'State vs Jane Smith', status: 'Hearing Scheduled' },
        // Add more cases as needed
    ];

    const notifications = [
        'Case 12345: New evidence submitted.',
        'Case 67890: Hearing scheduled for 10th September.',
        // Add more notifications as needed
    ];

    // Populate the ongoing cases list
    const casesList = document.getElementById('casesList');
    ongoingCases.forEach(caseInfo => {
        const listItem = document.createElement('li');
        listItem.textContent = `${caseInfo.caseTitle} - ${caseInfo.status} (Case No: ${caseInfo.caseNumber})`;
        casesList.appendChild(listItem);
    });

    // Populate the notifications list
    const notificationList = document.getElementById('notificationList');
    notifications.forEach(notification => {
        const listItem = document.createElement('li');
        listItem.textContent = notification;
        notificationList.appendChild(listItem);
    });
});


