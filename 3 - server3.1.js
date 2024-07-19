const express = require('express');
const multer = require('multer');
const xlsx = require('xlsx');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const port = 3000;

app.use(cors());

// Set up Multer to handle file uploads
const upload = multer();

// Define the path to the Excel file
const excelFilePath = path.join('C:/Users/PC/OneDrive/Desktop', 'MLBB_Draft_Data3.1.xlsx');

// Helper function to append data to the Excel file
const appendDataToExcel = (data) => {
  let workbook;

  // Check if the Excel file exists
  if (fs.existsSync(excelFilePath)) {
    // Read the existing file
    workbook = xlsx.readFile(excelFilePath);
  } else {
    // Create a new workbook
    workbook = xlsx.utils.book_new();
  }

  // Get the first worksheet or create a new one
  let worksheet = workbook.Sheets[workbook.SheetNames[0]];

  if (!worksheet) {
    // Define column headers
    worksheet = xlsx.utils.aoa_to_sheet([[
        'Match ID', 'Blue Team Name', 'Red Team Name', 'Blue Team 1st Ban', 'Red Team 1st Ban',
        'Blue Team 2nd Ban', 'Red Team 2nd Ban', 'Blue Team 3rd Ban', 'Red Team 3rd Ban',
        'Blue Team 1st Pick', 'Role Blue Team 1st Pick', 'Red Team 1st Pick', 'Role Red Team 1st Pick',
        'Red Team 2nd Pick', 'Role Red Team 2nd Pick', 'Blue Team 2nd Pick', 'Role Blue Team 2nd Pick',
        'Blue Team 3rd Pick', 'Role Blue Team 3rd Pick', 'Red Team 3rd Pick', 'Role Red Team 3rd Pick',
        'Red Team 4th Ban', 'Blue Team 4th Ban', 'Red Team 5th Ban', 'Blue Team 5th Ban',
        'Red Team 4th Pick', 'Role Red Team 4th Pick', 'Blue Team 4th Pick', 'Role Blue Team 4th Pick',
        'Blue Team 5th Pick', 'Role Blue Team 5th Pick', 'Red Team 5th Pick', 'Role Red Team 5th Pick',
        'Winning Team'
    ]]);
    xlsx.utils.book_append_sheet(workbook, worksheet, 'Sheet1');
}

  // Append the new data
  const jsonData = xlsx.utils.sheet_to_json(worksheet);
  jsonData.push(data);

  // Convert JSON back to worksheet
  const newWorksheet = xlsx.utils.json_to_sheet(jsonData);

  // Replace the old worksheet with the new one
  workbook.Sheets[workbook.SheetNames[0]] = newWorksheet;

  // Write the updated workbook to the file
  xlsx.writeFile(workbook, excelFilePath);
};

app.use(express.json());

app.post('/saveData', upload.none(), (req, res) => {
  const data = req.body;
  console.log('Received data:', data); // Log the received data
  appendDataToExcel(data);
  res.send('Data saved successfully');
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
