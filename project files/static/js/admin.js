// Function to sort the table by column
function sortTable(column) {
    const table = document.querySelector("table");
    const tbody = table.querySelector("tbody");
    const rows = Array.from(tbody.querySelectorAll("tr"));

    rows.sort((a, b) => {
        const aValue = a.querySelector(`td[data-${column}]`).textContent.trim();
        const bValue = b.querySelector(`td[data-${column}]`).textContent.trim();

        if (column === 'active') {
            return aValue.toLowerCase().localeCompare(bValue.toLowerCase());
        } else {
            return aValue.localeCompare(bValue, undefined, { numeric: true, sensitivity: 'base' });
        }
    });

    tbody.innerHTML = '';
    rows.forEach(row => tbody.appendChild(row));
}

// Function to filter the table based on the search input
function filterTable() {
    const input = document.getElementById("searchInput");
    const filter = input.value.toUpperCase();
    const table = document.querySelector("table");
    const tbody = table.querySelector("tbody");
    const rows = tbody.querySelectorAll("tr");

    rows.forEach(row => {
        const nameCell = row.querySelector("td[data-name]");
        const descriptionCell = row.querySelector("td[data-description]");

        if (nameCell && descriptionCell) {
            const nameText = nameCell.textContent.toUpperCase();
            const descriptionText = descriptionCell.textContent.toUpperCase();

            if (nameText.indexOf(filter) > -1 || descriptionText.indexOf(filter) > -1) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        }
    });
}

        // JavaScript to toggle the accordion panel
 var accordions = document.querySelectorAll(".accordion");

        accordions.forEach(function (accordion) {
            var panel = accordion.nextElementSibling; // Get the panel associated with the accordion
            accordion.addEventListener("click", function () {
                this.classList.toggle("active");
                if (panel.style.display === "block") {
                    panel.style.display = "none";
                } else {
                    panel.style.display = "block";
                }
            });
        });


