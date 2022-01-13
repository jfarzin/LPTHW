// Create needed constants
const list = document.querySelector('ul');
const titleInput = document.querySelector('#title');
const bodyInput = document.querySelector('#body');
const form = document.querySelector('form');
const submitBtn = document.querySelector('form button');

//create an instance of a db object for us to store the 
//open database in
let db;

window.onload = function() {
    //open db; it's created if it doesn't already exist. 
    //(see onupgradeneeded below)
    let request = indexedDB.open('notes_db', 1);

    //onerror handler signifies that the db didn't open 
    request.onerror = function() {
        console.log('Database failed to open.');
    };

    //onsuccess handler signifies that the database opened
    request.onsuccess = function() {
        console.log('Database opened successfully');

        //store the opened db object in the db var.
        //This is used a lot below
        db = request.result;

        //Run the displayData() function to display notes already in db
        displayData();
    };

    //setup the db tables if this has not already been done
    request.onupgradeneeded = function(e) {
        //Grab a reference to the opened db
        let db = e.target.result;

        //create an objectStore to store our notes in (basically like a single table)
        //including an auto-incrementing key
        let objectStore = db.createObjectStore('notes_os', { keyPath: 'id', autoIncrement:true });

        //Define what data items the objectStore will contain
        objectStore.createIndex('title', 'title', { unique: false });
        objectStore.createIndex('body', 'body', { unique: false });

        console.log('Db setup complete.');
    };

    //create an onsubmit handler so that when form is submitted the addData() function runs
    form.onsubmit = addData;

    function addData(e) {
        //prevent default - we don't want to submit in conventional way
        e.preventDefault();

        //grab the new values entered into the form fields and store them in an 
        //object ready for being inserted into the new db
        let newItem = { title: titleInput.value, body: bodyInput.value };

        //open a read/write db transaction, ready for adding new data
        let transaction = db.transaction(['notes_os'], 'readwrite');

        //call an object store that's already been added to the db
        let objectStore = transaction.objectStore('notes_os');

        //make a request to add our newItem object to the objectStore
        let request = objectStore.add(newItem);
        request.onsuccess = function() {
            //clear the form, ready for adding next entry
            titleInput.value = '';
            bodyInput.value = '';
        };

        //report on the success of the transaction completing, when everything done
        transaction.oncomplete = function() {
            console.log('Transaction completed: db modification finished.');

            //update the display of data to show the newly added item, by running displayData() again
            displayData();
        };
    };

    function displayData() {
        //Here we empty the contents of the list element each time the display is updated
        //if you didn't, you'd get duplicates listed each time a new note is added
        while (list.firstChild) {
            list.removeChild(list.firstChild);
        };

        //open our object store and then get a cursor - which iterates through all the 
        //different data items in the store
        let objectStore = db.transaction('notes_os').objectStore('notes_os');
        objectStore.openCursor().onsuccess = function(e) {
            //Get a reference to the cursor
            let cursor = e.target.result;

            //if there is still another data item to iterate through, keep runnning this code
            if(cursor) {
                //create a list item, h3, and p to put each data item inside when displaying it
                //structure the HTML format and append it inside the list
                const listItem = document.createElement('li');
                const h3 = document.createElement('h3');
                const para = document.createElement('p');

                listItem.appendChild(h3);
                listItem.appendChild(para);
                list.appendChild(listItem);

                //put the data from the cursor inside the h3 and para
                //h3.textContent = 'next note';
                h3.textContent = cursor.value.title;
                para.textContent = cursor.value.body;

                //store the ID of the data item inside an attribute on the listItem, so we know
                //which item it corresponds to. This will be useful later when we want to delete items
                listItem.setAttribute('data-note-id', cursor.value.id);

                //create a button and place it inside each listItem
                const deleteBtn = document.createElement('button');
                listItem.appendChild(deleteBtn);
                deleteBtn.textContent = 'Delete';

                //set an event handler so that when the button is clicked, the deleteItem()
                //function is run
                deleteBtn.onclick = deleteItem;

                //iterate to next item in the cursor
                cursor.continue();              
            } else {
                //Again, if list item is empty, display a 'no notes' message
                if (!list.firstChild) {
                    const listItem = document.createElement('li');
                    listItem.textContent = 'No notes stored.';
                    list.appendChild(listItem);
                }
                //if there are not more cursor items to iterate through --> say so
                console.log('Notes all displayed.');
            }
        };
    }

    function deleteItem(e) {
        //retrieve the name of the task we want to delete. We need
        //to convert it to a number before trying it use it with the IDB;
        //IDB key values are case-sensitive
        let noteId = Number(e.target.parentNode.getAttribute('data-note-id'));

        //open a database transaction and delete the task, finding it using the id we retrieved above
        let transaction = db.transaction(['notes_os'], 'readwrite');
        let objectStore = transaction.objectStore('notes_os');
        let request = objectStore.delete(noteId);

        //report that the data item has been deleted
        transaction.oncomplete = function() {
            //delete the parent of the button
            //which is the list item, so it is no longer displayed
            e.target.parentNode.parentNode.removeChild(e.target.parentNode);
            console.log('Note' + noteId + 'deleted.');

            //again, if list item is empty, display message
            if (!list.firstChild) {
                let listItem = document.createElement('li');
                listItem.textContent = 'No notes stored.';
                list.appendChild(listItem);
            }
        };
    }
};