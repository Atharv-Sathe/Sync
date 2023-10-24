const express = require('express');

const multer = require('multer');

const app = express();
const port = 3000;

const path = require('path');

const fileStorageEngine = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, './files')
    },
    filename: (req, file, cb) => {
        const parts = file.mimetype.split('/');
        cb(null, Date.now() + "--" + file.originalname);
    }
});

const upload = multer({ storage : fileStorageEngine });

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'upload.html'));
});

app.post('/single', upload.single('spreadsheet'), (req, res) => {
    console.log(req.file);
    res.send('Single file upload successful!');
});

app.post('/multiple', upload.array('spreadsheets', 3), (req, res) => {
    console.log(req.files);
    res.send('Multiple file upload successful!');
});

app.use(express.static('public'));

app.listen(3000, () => console.log('Server running on port 3000'));
