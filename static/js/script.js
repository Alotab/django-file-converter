


//======================PROCESS FILES ============================//
// `handleFilesSelected` function displays all the files uploaded by the user to the screen


const fileIn = document.getElementById('file-input');
const selectedFiles = document.getElementById('files-list');

let fileList = [];

function handleFilesSelected(){
    const selectFiles = [...fileIn.files];
    for (const f of selectFiles){
        // console.log(f.type);
        // fileList.push(f);
        const li = document.createElement('li');
        li.classList.add('file-list');
        // li.id = `${f.name}-moses`;

        const insert = formatSizeUnits(f.size);
        li.innerHTML = `
                          <div class="file-name-wrapper" id=file-${f.name}>
                              <span class="file-name-icon"></span>
                              <p>${f.name}</p>
                          </div>
                        
                          <div class="select-conversion-container">
                          <!--    <span>to</span> -->
                              <div class="conversion">
                                  <button class="btn-button btn-caret btn btn-sm btn-outline-dark" id="formatSelect"></button>
                                  <!-- <div class="select-convertor"> -->
                                      
                                      <!-- <div class="enclose"> -->
                                  <div class="dropdown-menu select-choice-container select-format" style="display: none;">
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
                                                      <li class="current format-btn btn-secondary"><span>PDF</span></li>
                                                      <li class="current format-btn btn-secondary"><span>BEEP</span></li>
                                                      <li class="current format-btns btn-secondarys"><span>JPG</span></li>
                                                      
                                                      <li class="current format-btns btn-secondarys"><span>JPEG</span></li>
                                                      <li class="current format-btns btn-secondarys"><span>XLSX</span></li>
                                                      <li class="current format-btns btn-secondarys"><span>XLS</span></li>
                                                      <li class="current format-btns btn-secondarys"><span>CSV</span></li>
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
                          </div>
                          
                          <div class="close-button">
                              <i class="ri-close-line"></i>
                          </div>
        
                        `;
        selectedFiles.appendChild(li);

        //====== append file type icon/symbol to every uploaded file =====//
        const fileIconWrapper = li.querySelector('.file-name-wrapper');
        const fileIcon = fileIconWrapper.querySelector('.file-name-icon');
        const audioVideoTypes = ['video/mp4', 'video/mp3', 'video/avi', 'video/mov','video/wmv','video/mkv','video/ogg','video/flv','video/webm','video/f4v', 'video/swf','video/mpeg','audio/avi', 'audio/wav', 'audio/aac', 'audio/flac', 'audio/mkv', 'audio/aiff', 'audio/mpeg', 'audio/mp3', 'audio/mp4'];
        const fileIsPresent = audioVideoTypes.includes(f.type);

        if(f.type === 'image/jpeg'){
            fileIcon.style.backgroundImage = 'url("data:image/svg+xml;charset=utf8,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' fill=\'%23a067e6\' width=\'24\' height=\'24\' viewBox=\'0 0 24 24\'%3E%3Cpath d=\'M7,8.5C7,7.119,8.119,6,9.5,6S12,7.119,12,8.5S10.881,11,9.5,11S7,9.881,7,8.5z M14.5,11l-4,6l-2-3L5,19h15L14.5,11z\'/%3E%3C/svg%3E")';
        } else if(f.type === 'application/vnd.ms-excel' || f.type === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'){
            fileIcon.style.backgroundImage = 'url("data:image/svg+xml;charset=utf8,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' fill=\'%234fcb4b\' width=\'24\' height=\'24\' viewBox=\'0 0 24 24\'%3E%3Cpath d=\'M5,17.33V6.67L15,4v16L5,17.33z M19,6h-3v12h3V6z M12.852,15.5l-2.08-3.5l2.043-3.5H11.57l-1.244,2.246c-0.047,0.196-0.125,0.382-0.232,0.554c-0.088-0.173-0.158-0.354-0.209-0.539L8.684,8.5H7.338L9.33,12l-2.182,3.5h1.338l1.396-2.416c0.066-0.139,0.117-0.385,0.139-0.385c0.061,0.124,0.104,0.252,0.131,0.385l1.381,2.416H12.852L12.852,15.5z\'/%3E%3C/svg%3E")';

        } else if(f.type === 'application/pdf') {
            fileIcon.style.backgroundImage = 'url("data:image/svg+xml;charset=utf8,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' fill=\'%23fd1e1e\' width=\'24\' height=\'24\' viewBox=\'0 0 24 24\'%3E%3Cpath d=\'M17.611,13.224c-0.336-0.115-0.752-0.159-1.242-0.15c-0.281,0.007-0.562,0.027-0.84,0.06c-0.319,0.037-0.636,0.098-0.952,0.158c-0.314-0.308-0.627-0.618-0.906-0.958c-0.662-0.808-1.231-1.684-1.732-2.599c0.087-0.197,0.176-0.397,0.257-0.608c0.11-0.284,0.207-0.56,0.283-0.825c0.153-0.528,0.227-0.985,0.192-1.37c-0.117-1.353-0.86-2.218-1.89-2.127c-1.031,0.09-1.617,1.074-1.5,2.426c0.031,0.354,0.16,0.752,0.369,1.196c0.111,0.24,0.244,0.488,0.396,0.743c0.172,0.291,0.364,0.569,0.559,0.846c-0.044,0.116-0.087,0.233-0.132,0.349c-0.363,0.953-0.736,1.901-1.119,2.846c-0.221,0.549-0.462,1.089-0.705,1.628c-0.024,0.004-0.042,0.007-0.068,0.012c-0.256,0.047-0.525,0.104-0.797,0.17c-0.283,0.068-0.563,0.148-0.838,0.24c-0.521,0.178-0.937,0.38-1.232,0.63c-1.041,0.871-1.324,1.978-0.658,2.769c0.665,0.791,1.807,0.707,2.848-0.164c0.272-0.229,0.523-0.563,0.769-0.988c0.131-0.229,0.259-0.48,0.381-0.75c0.078-0.17,0.137-0.349,0.207-0.522l0.173-0.364c1.191-0.38,2.396-0.717,3.614-1c0.391-0.093,0.785-0.173,1.179-0.256c0.149,0.166,0.303,0.335,0.469,0.502c0.215,0.218,0.428,0.418,0.639,0.595c0.42,0.354,0.808,0.606,1.174,0.733c1.283,0.442,2.376,0.115,2.712-0.862C19.555,14.602,18.895,13.667,17.611,13.224zM10.879,5.941c0.314-0.028,0.595,0.3,0.663,1.089c0.019,0.215-0.034,0.546-0.15,0.95c-0.067,0.227-0.261,0.784-0.263,0.789l-0.001,0c-0.007-0.012-0.359-0.63-0.453-0.831c-0.156-0.333-0.248-0.613-0.265-0.807C10.342,6.342,10.564,5.969,10.879,5.941zM7.683,16.947c-0.183,0.32-0.36,0.555-0.51,0.68c-0.606,0.508-1.039,0.54-1.242,0.298c-0.202-0.241-0.096-0.66,0.511-1.168c0.166-0.14,0.467-0.286,0.864-0.421c0.226-0.077,0.8-0.24,0.8-0.24S7.796,16.752,7.683,16.947z M12.787,13.756c-0.921,0.215-1.832,0.467-2.739,0.735c0.112-0.265,0.229-0.543,0.353-0.847l0.193-0.475c0.277-0.69,0.539-1.387,0.807-2.082c0.417,0.673,0.878,1.344,1.4,1.976c0.166,0.201,0.338,0.391,0.51,0.579C13.137,13.682,12.961,13.715,12.787,13.756z M18.138,15.208c-0.103,0.298-0.517,0.422-1.265,0.163c-0.203-0.07-0.484-0.254-0.805-0.524c-0.209-0.184-0.415-0.371-0.617-0.562c0,0,0.722-0.071,0.947-0.075c0.367-0.009,0.66,0.022,0.844,0.086C17.99,14.554,18.24,14.908,18.138,15.208z\'/%3E%3C/svg%3E")';
        } else if(fileIsPresent) {
            fileIcon.style.backgroundImage = 'url("data:image/svg+xml;charset=utf8,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' fill=\'%233aa8ff\' width=\'24\' height=\'24\' viewBox=\'0 0 24 24\'%3E%3Cpath d=\'M12,19c-3.866,0-7-3.134-7-7s3.134-7,7-7s7,3.134,7,7S15.866,19,12,19z M10,8v8l6-4L10,8z\'/%3E%3C/svg%3E")';
        } else {
            fileIcon.style.backgroundImage = 'url("data:image/svg+xml;charset=utf8,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' fill=\'%23a067e6\' width=\'24\' height=\'24\' viewBox=\'0 0 24 24\'%3E%3Cpath d=\'M7,8.5C7,7.119,8.119,6,9.5,6S12,7.119,12,8.5S10.881,11,9.5,11S7,9.881,7,8.5z M14.5,11l-4,6l-2-3L5,19h15L14.5,11z\'/%3E%3C/svg%3E")';
        };



        //========= Delete any of the Uploaded files =========//
        const deleteButton = li.querySelector('.close-button');
        deleteButton.addEventListener('click', () => {
          li.remove();
        });


        const buttonClick = li.querySelector('.btn');
        const activateDrop = li.querySelector('.dropdown-menu');
        const formatItems = li.querySelector('#format-list');

       

        //========= Popup Format type list when button is clicked  ========//

        if(buttonClick) {
            buttonClick.addEventListener('click', () => {
                if(activateDrop.style.display === "none") {
                    activateDrop.style.display = "block";
                } else {
                    activateDrop.style.display = "none";
                }
            });
        };

        // Hide the format div when the user clicks anywhere on the screen
        window.onclick = function(event) {
            if (event.target != buttonClick) {
                activateDrop.style.display = "none";
            }
        }


       //========= Display type of format user selected ========//
       const mydisplay = () => {
        return `none`;
        };
        let selectedFormats = [];
        if(formatItems){
          formatItems.querySelectorAll('li span').forEach(format => {
            format.addEventListener('click', () => {
            //   activateDrop.classList.remove('activate');
              activateDrop.style.display = "none";

              buttonClick.textContent = format.textContent;

              buttonClick.style.setProperty('--display', mydisplay());
            //   selectedFormats.push(format.textContent);
            });
          });
        };

    };
};

document.getElementById('file-input').addEventListener('change', handleFilesSelected, false);



// const fileInput = document.querySelector('#file-input');
const fileInput = document.getElementById('file-input');
const formatSelects = document.querySelectorAll('.btn-button');
const formatSele = document.querySelector('.btn-button');
const convertButton = document.querySelector('.convert');

const selectForma = document.getElementById('formatSelect');

// const removeFormatSelector = document.querySelector('.btn');







convertButton.addEventListener('click', ()=> {


    // observer.takeRecords();

    // removeFormatSelector.style.display = 'none';
    // console.log('hideen');
    // console.log(convertButton);
    // console.log(removeFormatSelector);
    // if(removeFormatSelector) {
    //     // removeFormatSelector.classList.add('hidden');
    //     console.log(removeFormatSelector);
        
    // }
   


    // document.getElementById('download-links').classList.toggle('hidden');

    // document.getElementById('download-links').classList.add('act');

    // console.log(this.crypto.randomUUID());
    // console.log('hi');

    // const selectForma = document.querySelectorAll('#formatSelect');
    // selectForma.forEach(format => {
    //     var takeout = format.textContent;
      
    // })
    
})

fileInput.addEventListener('change', filefileHandle, false);
const lisltlist = [];
function filefileHandle() {
    const fileLists = this.files;
}



// convertButton.addEventListener('click', () => {
//     // var formats = Array.from(buttonClick).map(select => select);
//     var tryy = selectForma.forEach(forma => {
//         forma.textContent;
//     }) 
//     // var takeout = selectForma.textContent;

// });



// This function loops through all the format buttons
// Checks and remove a button if a selected format has been assigned to it after conversion is done
function checkElementContent(elements) {
    for (const ele of elements){
        if(ele.textContent){
            ele.style.display = "none";
        };
    };
}


// Apppends the converetd file to the download-link class to the original file div
function appendDownloadLink(fileId, downloadUrl) {

    const downloadLink = document.createElement('a');
    downloadLink.href = downloadUrl;
    downloadLink.textContent = 'Download';

    try {
        const parentDiv = document.querySelector(`[data-file-id="${fileId}"]`).parentNode;
        const parentFileDiv = document.querySelector(`[data-file-id="${fileId}"]`).parentElement;
        const downloadEl = parentDiv.querySelector('.download-link');

        if(parentDiv) {
            if(!downloadEl.querySelector('a')) {
                downloadEl.appendChild(downloadLink);
            };
        };

        // update file status before and after conversion
        // remove format button after conversion is complete
        if(parentFileDiv){
            const fileStatus = parentFileDiv.querySelector('.status');
            const readyNotice = fileStatus.querySelector('.spining-ready')
            const completeNotice = fileStatus.querySelector('.spining-finish')
            readyNotice.style.display = "none";
            completeNotice .style.display = "block";

            
            const conversionContainer = parentFileDiv.querySelector('.select-conversion-container');
            const conversion = conversionContainer.querySelector('.conversion');
            const conversionbutton = conversion.querySelector('.btn');
            conversionbutton.style.display = "none";
        };
    } catch (error) {
        // console.log("parentDiv is empty");
    };
}




// AJAX code sends uploaded file data (formData) to the django backend view function and returns a `response`
// Process response to display converted file on the screen for user download
const fileIds = [];
const formData = new FormData();
convertButton.addEventListener('click', (event) => {
    event.preventDefault();

    const selectFiles = [...fileIn.files];
    for(const file of selectFiles){
        const filename = file.name;
        formData.append('files', file, filename);

        // create unique uuid, assign to each file and append the uuid to the formData
        const fileId = `${filename}_` + Math.floor((Math.random() * 1000000) + 1);
        const fileDiv = document.getElementById(`file-${filename}`);
        // const fileIdentifier = document.getElementById(`${filename}-moses`);
        if(fileDiv) {
            fileDiv.dataset.fileId = fileId;
            // fileIdentifier.dataset.fileId = fileId;
        }
        
        formData.append('uuid', fileId);
    }

    const files = fileInput.files;
    const selectForma = document.querySelectorAll('#formatSelect');
        
    // Convert NodeList to an array and extract text content
    const formats = Array.from(selectForma).map(format => format.textContent);

    for(const format of formats) {
        formData.append('formats', format);
    }

  
    $.ajax({
        type: 'POST',
        url: "/upload/",
        data: formData,
        processData: false,
        contentType: false,
        success: function(res) {
            // debugger;

            var context = JSON.parse(res);
            // console.log(context);
            if(context){
                var downloadUrls = context.converted_files.map(function(converted_File) {
                    return converted_File.download_url;
                });
        
    
                var originalFilename = context.converted_files.map(function(converted_File) {
                    return converted_File.original_filename;
                });

                for (const convertedFile of context.converted_files) {
                    if(convertedFile.converted_filename !== null){
                        appendDownloadLink(convertedFile.uuid, convertedFile.download_url);

                    }
                };
            };
        },
        error: function(err) {
            console.log(err);
        }
    });
});




// converts file sizes from bytes to megabytes, kilibytes and gigabytes
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
  
  
// Assigns units to the filesize `MB`, `GB`, `KB`
function checkFileSize(f){
    const file = document.querySelector('#file-input').files[0];
  
    const fileSizeInBytes = f.size;
  
    const fileSizeInKBOrMB = fileSizeInBytes < 1024 ? fileSizeInBytes / 1024 : fileSizeInBytes / (1024 * 1024);
  
    const roundedFileSizeInKBOrMB = Math.ceil(fileSizeInKBOrMB);
    console.log("rounded ", roundedFileSizeInKBOrMB);
  
    const fileSizeElement = document.querySelector('.file-size');
    const insertAllo = `${roundedFileSizeInKBOrMB} ${fileSizeInBytes < 1024 ? 'KB' : 'MB'}`
  
    fileSizeElement.textContent = insertAllo;
}
  












// function downloadCSVFile(csvFile) {
//     // get filename
//     const filename = csvFile.name;

//     // Create a link to download the CSVFile
//     const donwloadLinkParent = document.querySelector('.download-link');
//     const link = document.createElement('a');
//     link.href = URL.createObjectURL(csvFile);
//     link.download = filename;

//     donwloadLinkParent.appendChild(link);

//     link.click();
// }













































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
