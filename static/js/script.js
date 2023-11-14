

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
        // console.log('onchange ',f);
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
                                  <button class="btn-button btn-caret btn btn-sm btn-outline-dark" id="formatSelect"></button>
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
                            <a "{% url 'download'%}">Download</a>
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
}

document.getElementById('file-input').addEventListener('change', handleFilesSelected, false);



// const fileInput = document.querySelector('#file-input');
const fileInput = document.getElementById('file-input');
const formatSelects = document.querySelectorAll('.btn-button');
const convertButton = document.querySelector('.convert');

const selectForma = document.getElementById('formatSelect');


convertButton.addEventListener('click', ()=> {
    // document.getElementById('download-links').classList.toggle('hidden');
    document.getElementById('download-links').classList.add('act');



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


const selectedFormats = [];

// convertButton.addEventListener('click', () => {
//     var files = fileInput.files;
//     const selectForma = document.querySelectorAll('#formatSelect');

//     var formats = selectForma.forEach(format => {
//         const listFormats = format.textContent;
//         selectedFormats.push(listFormats);
//     });

//     console.log(selectedFormats);
  
    
//     var formData = new FormData();
//     Array.from(files).forEach((file, index)=> {
//         formData.append('files', file);
//         // formData.append('formats', formats[index]);
//         formData.append('formats', selectedFormats[index]);
//     });

//     $.ajax({
//         type: 'POST', 
//         url: "/upload/",
//         data: formData,
//         processData: false,
//         contentType: false,
//         success: function(res) {
//             console.log('Data successfully transfer');
//         },
//         error: function(err) {
//             console.log(err);
//         }
    
//     });

// });

// const selectedFormats = [];


convertButton.addEventListener('click', () => {
    const formData = new FormData();
    const selectFiles = [...fileIn.files];
    console.log(selectFiles);
    for(const file of selectFiles){
        const filename = file.name
        console.log(filename)
        formData.append('files', file, filename)
        // console.log(formData);
    }

    // console.log(selectFiles);
    const files = fileInput.files;
    // console.log(files);
    const selectForma = document.querySelectorAll('#formatSelect');
        
    // Convert NodeList to an array and extract text content
    const formats = Array.from(selectForma).map(format => format.textContent);

    for(const format of formats) {
        formData.append('formats', format)
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
           
            // var converted_file_name = context.converted_files[0].download_url;
            // document.getElementById('list-item').textContent = converted_file_name;
            console.log(context.converted_files);

            var downloadUrls = context.converted_files.map(function(converted_File) {
                return converted_File.download_url;
            })
            console.log(downloadUrls);

            var originalFilename = context.converted_files.map(function(converted_File) {
                return converted_File.original_filename;
            })
            console.log(originalFilename);

            for (var i = 0; i < downloadUrls.length; i++) {
                var downloadLink = document.createElement('a');
                downloadLink.href = downloadUrls[i];
                downloadLink.textContent = 'Download converted file for ' + originalFilename[i];


                document.getElementById('list-item').appendChild(downloadLink);

                var convertedFile = document.createElement('a');
                convertedFile.href = downloadUrls[i];
                convertedFile.textContent = originalFilename[i];

                document.getElementById('list-item').appendChild(convertedFile);
            }






            // // Get the download URL from the response
            // var downloadUrl = context.converted_files[0].download_url;

            // // Create a new element to display the download link
            // var downloadLink = document.createElement('a');
            // downloadLink.href = downloadUrl;
            // downloadLink.textContent = 'DOWNLOAD';

            // // Append the download link to the DOM
            // document.getElementById('list-item').appendChild(downloadLink);

    
           

        //    for(var i = 0; i < converted_files.length; i++){
        //     var converted_file = converted_files[i];
        //     console.log(converted_file)

        //    }
        },
        error: function(err) {
            console.log(err);
        }
    });
});











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
