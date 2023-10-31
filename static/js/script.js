

// const dropEl = document.querySelector(".drop-down");
// const dropEl = document.querySelector(".drop-down");
// const dropdownEl = document.querySelector('.drop-down-list');

// dropEl.addEventListener('click', () => {
//     console.log('hi');
//     dropdownEl.classList.add('active');


//     document.addEventListener('mousedown', (e) => {
//         e.preventDefault();
//         dropdownEl.classList.remove('active');
//     });
  
// })

document.getElementById('file-input').addEventListener('change', function() {
    var form = document.getElementById('file-form');
    var formData = new FormData(form);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', form.action);
    xhr.onload = function() {
        if (xhr.status === 200) {
            // Update the page with the uploaded files
            // For example, you could display a list of links to the uploaded files
        } else {
            alert('An error occurred!');
        }
    };
    xhr.send(formData);
});


// var form = document.getElementById('file-form');
// var formData = new FormData(form);

// $.ajax({
//     type: 'POST',
//     url: '/upload',
//     headers: {
//         'X-CSRFToken' : $('meta[name="csrf-token"]').attr('content')
//     },
//     data: formData,
//     processData:false,
//     contentType: false,
//     success: function(data) {

//     }
// });

// document.getElementById('file-form').addEventListener('change', function(e) {
//     e.preventDefault();
//     var xhr = new XMLHttpRequest();

//     xhr.open('POST', this.action);
//     xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

//     xhr.send(new FormData(this));

//     xhr.onload = function() {
//         if(xhr.status === 200){

//         }else{

//         }
//     };
// });







//======================PROCESS FILES ============================//
// const filename = files.name;
// const filesize = files.size;
// const realsizeMegabyte = filesize / 1048576;
// const realsizekb = filesize / 1024;


const fileIn = document.getElementById('file-input');
const selectedFiles = document.getElementById('files-list');

let fileList = [];

function handleFilesSelected(){
    const selectFiles = [...fileIn.files];
    for (const f of selectFiles){
        // fileList.push(f);
        // console.log(fileList);
        const li = document.createElement('li');
        li.classList.add('file-list');

        const insert = formatSizeUnits(f.size);
        li.innerHTML = `
                          <div class="file-name-wrapper">
                              <span class="file-name-icon"></span>
                              <p>${f.name}</p>
                          </div>
                        
                          <div class="select-conversion-container">
                              <span>to</span>
                              <div class="conversion">
                                  <button class="btn-button btn-caret btn btn-sm btn-outline-dark"> <i></i></button>
                                  <!-- <div class="select-convertor"> -->
                                      
                                      <!-- <div class="enclose"> -->
                                  <div class="dropdown-menu select-choice-container select-format show">
                                  <!-- <div class="dropdown-menu"> -->
                                      <div class="format-search">
                                          <input class="form-search" type="text" placeholder="Search">
                                          <i class="ri-search-line search-icon"></i>
                                          <i class="ri-close-fill search-reset"></i>
                                      </div> 
                              
                                      <div class="wrapper">
                                          <ul class="types">
                                              <li class="current">Image</li>
                                              <li class="current">Document</li>
                                              <li class="current">Ebook</li>
                                              <li class="current">Font</li>
                                              <li class="current">Vector</li>
                                          </ul>
                                          <div class="formats">
                                              <div class="format-inner">
                                                  <ul id="format-list">
                                                      <li class="current format-btn btn-secondary"><span>PNG</span></li>
                                                      <li class="current format-btn btn-secondary"><span>GIF</span></li>
                                                      <li class="current format-btn btn-secondary"><span>BEEP</span></li>
                                                      <li class="current format-btns btn-secondarys"><span>JPG</span></li>
                                                      
                                                      <li class="current format-btns btn-secondarys"><span>JPEG</span></li>
                                                  </ul>
                                              </div>
                                          </div>
                                      </div>
                                  </div>
                                      <!-- </div> -->
                                  <!-- </div> -->
                              </div>
                          </div>

                          <div class="status">
                              <span class="spining-ready">Ready</span>
                              <span class="spining-finish">Finished</span>
                              <i class="ri-refresh-line"></i>
                          </div>

                          <div class="file-size">${insert}</div>
                          <div class="download-link">
                              <a href="">Download</a>
                          </div>
                          <div class="close-button">
                              <i class="ri-close-line"></i>
                          </div>
        
                        `;
        selectedFiles.appendChild(li);

        //========= Delete any of the Uploaded files =========//
        const deleteButton = li.querySelector('.close-button');
        deleteButton.addEventListener('click', () => {
          li.remove();
        });



        const buttonClick = li.querySelector('.btn-button');
        const activateDrop = li.querySelector('.dropdown-menu');
        const formatItems = li.querySelector('#format-list');

       

        //========= Popup Format type list when button is clicked  ========//
        // if(buttonClick){
        //     buttonClick.addEventListener('click', () => {
        //       activateDrop.classList.add('activate');
        //     });
        // };
        var currentDay = null;

        // if(buttonClick ){
        //     buttonClick.addEventListener('click', () => {
        //         if(currentDay && currentDay !== activateDrop){
        //             // activateDrop.style.display = "none";
        //         }
        //     });
        // };

        if(buttonClick){
            buttonClick.addEventListener('click', function(e){
                e.stopPropagation();
                if(currentDay && currentDay !== activateDrop){
                    activateDrop.style.display = "none";
                    // console.log('yes');
                }
                if(activateDrop.style.display === "none") {
                    activateDrop.style.display = "block";
                    currentDay = activateDrop;
                } else {
                    activateDrop.style.display = "none";
                    currentDay = null;
                }
            });
        };

        document.addEventListener('click', function(){
            if(currentDay){
                currentDay.style.display = "none";
                currentDay  = null;
            }
            // activateDrop.style.display = "none"; 
        })


       //========= Display type of format user selected ========//
       const mydisplay = () => {
        return `none`;
        };

        if(formatItems){
          formatItems.querySelectorAll('li span').forEach(format => {
            format.addEventListener('click', () => {
            //   activateDrop.classList.remove('activate');
              activateDrop.style.display = "none";

              buttonClick.textContent = format.textContent;

              buttonClick.style.setProperty('--display', mydisplay());
            });
          });
        };

    };
}






// Convert any File 
function convertFiles(){
    // Get the file types of the files in the file list
    const fileTypes = fileList.map(file => file.type);

    // Check if all files are PDF files
    if(fileTypes.every(type => type === 'application/pdf')) {
        // Convert the files to CSV files
        const csvFiles = fileList.map(file => convertPDFToCSV(file));
        console.log(csvFiles);
        // Download the CSV files
        // csvFiles.forEach(csvFile => downloadCSVFile(csvFile));
     
    } else {
        console.log('The files you entered are not PDF ....');
    }
    
}

document.getElementById('file-input').addEventListener('change', handleFilesSelected, false);
// document.querySelector('.convert').addEventListener('click', convertFiles);


// Convert PDF -> CSV
async function convertPDFToCSV(file){
    const csvFile = new Blob([file], {'type': 'application/csv'});
    // console.log(csvFile);
   
    // Download the CSV file
    return csvFile;
}

function downloadCSVFile(csvFile) {
    // get filename
    const filename = csvFile.name;

    // Create a link to download the CSVFile
    const donwloadLinkParent = document.querySelector('.download-link');
    const link = document.createElement('a');
    link.href = URL.createObjectURL(csvFile);
    link.download = filename;

    donwloadLinkParent.appendChild(link);

    link.click();
}

function formatSizeUnits(bytes) {
  if (bytes >= 1073741824) {
      bytes = (bytes / 1073741824).toFixed(2) + " GB";
  } else if (bytes >= 1048576) {
      bytes = (bytes / 1048576).toFixed(2) + " MB";
  } else if (bytes >= 1024) {
      bytes = (bytes / 1024).toFixed(2) + " KB";
  } else if (bytes > 1) {
      bytes = bytes + " bytes";
  } else if (bytes == 1) {
      bytes = bytes + " byte";
  } else {
      bytes = "0 bytes";
  }
  return bytes;
}

function checkFileSize(f){
  const file = document.querySelector('#file-input').files[0];

  const fileSizeInBytes = f.size
  // const fileSizeInBytes = file.size;

  const fileSizeInKBOrMB = fileSizeInBytes < 1024 ? fileSizeInBytes / 1024 : fileSizeInBytes / (1024 * 1024);

  const roundedFileSizeInKBOrMB = Math.ceil(fileSizeInKBOrMB);
  console.log("rounded ", roundedFileSizeInKBOrMB);

  // const fileSizeElement = li.querySelector('.file-size');
  const fileSizeElement = document.querySelector('.file-size');
  const insertAllo = `${roundedFileSizeInKBOrMB} ${fileSizeInBytes < 1024 ? 'KB' : 'MB'}`

  fileSizeElement.textContent = insertAllo;



}

// const buttonClick = li.querySelector('.btn-button');
const activateDrop = document.querySelector('.dropdown-menu');
// const formatItems = li.querySelector('#format-list');

// if(buttonClick){
//     buttonClick.addEventListener('click', () => {
//       activateDrop.classList.add('activate');
//     });
// };




// buttonClick.addEventListener('click', () => {
//     //       activateDrop.classList.add('activate');











































//========= Display type of format user selected ========//
// const formatList = document.getElementById('format-list');
// const textInput = document.querySelector('.select-convertor');

// let selectedLabel = false;
// if(formatList){
//     formatList.querySelectorAll('li').forEach( listItem => {
//         listItem.addEventListener('click', (e) => {
//             const label = listItem.querySelector('span').textContent;
//             if(textInput.textContent !== label){
//               e.preventDefault();
//               textInput.textContent = label;
//               selectedLabel = true;
//             }
//         });
//     })
// }


/// Try again and again
// const buttonClick = document.querySelector('.btn-button');
// const activateDrop = document.querySelector('.dropdown-menu');


// const textInput = document.querySelector('.select-convertor');
// const beforeElement = document.querySelector('.btn-button::before');

// if(buttonClick){
//   buttonClick.addEventListener('click', () => {
//     activateDrop.classList.add('activate');
//   });
// }



// const formatItems = document.getElementById('format-list');
// const activateDrop = document.querySelector('.dropdown-menu');
// const buttonClick = document.querySelector('.btn-button');
// if(formatItems){
//   formatItems.querySelectorAll('li span').forEach(format => {
//     // console.log(format.textContent);
//     format.addEventListener('click', () => {
//       activateDrop.classList.remove('activate');

//       buttonClick.textContent = format.textContent;
      
//       const root = document.querySelector(":root");
//       root.style.setProperty("--display", 'none');

//     });
//   });
// }
