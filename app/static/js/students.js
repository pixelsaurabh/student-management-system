const editButtons = document.querySelectorAll(".btn-edit");

editButtons.forEach((button) => {

    button.addEventListener("click", () => {

        document.getElementById("editStudentId").value =
            button.dataset.id;

        document.getElementById("editName").value =
            button.dataset.name;

        document.getElementById("editUniversityRollNumber").value =
            button.dataset.universityRollNumber;

        document.getElementById("editBranch").value =
            button.dataset.branch;

        document.getElementById("editYear").value =
            button.dataset.year;

        document.getElementById("editSection").value =
            button.dataset.section;

        document.getElementById("editEmail").value =
            button.dataset.email;

        document.getElementById("editPhone").value =
            button.dataset.phone;

    });

});

// ==========================
// Live Student Search
// ==========================

const searchInput = document.getElementById("searchStudent");

searchInput.addEventListener("keyup", () => {

    const searchValue = searchInput.value.toLowerCase();

    const rows = document.querySelectorAll(".student-table tbody tr");

    let visibleRows = 0;

    rows.forEach((row) => {

        const rowText = row.innerText.toLowerCase();

        if (rowText.includes(searchValue)) {

            row.style.display = "";

            visibleRows++;

        } else {

            row.style.display = "none";

        }

    });

    const noResults = document.getElementById("noResultsMessage");

    if (visibleRows === 0) {

        noResults.style.display = "block";

    } else {

        noResults.style.display = "none";

    }

});

// ==========================
// Delete Student
// ==========================

const deleteButtons = document.querySelectorAll(".btn-delete");

deleteButtons.forEach((button) => {

    button.addEventListener("click", () => {

        document.getElementById("deleteStudentId").value =
            button.dataset.id;

        document.getElementById("deleteStudentName").textContent =
            button.dataset.name;

        document.getElementById("deleteUniversityRollNumber").textContent =
            button.dataset.universityRollNumber;

    });

});