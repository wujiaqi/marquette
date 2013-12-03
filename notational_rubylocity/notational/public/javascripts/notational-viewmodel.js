define(['jquery', 'knockout'], function($, ko) {

	function GetDate() {
		var today = new Date();
		var dd = today.getDate();
		var mm = today.getMonth() + 1;
		//January is 0!

		var yyyy = today.getFullYear();
		//if(dd<10){dd='0'+dd} if(mm<10){mm='0'+mm} today = mm+'/'+dd+'/'+yyyy;
		return today.toLocaleTimeString() + " " + today.toLocaleDateString();
	}

	//model for a note object
	function Note(id, newTitle, contents) {
		var self = this;
		self.noteId = id;
		self.noteTitle = newTitle;
		self.modified = ko.observable(GetDate());
		self.contents = ko.observable(contents);
	}

	//viewmodel for the application
	function NoteViewModel() {
		var self = this;

		//keep track of next available ID
		self.noteIdTracker = 0;

		//value of search bar
		self.searchBarValue = ko.observable("");

		//value of textarea
		self.textAreaValue = ko.observable("");

		//current note being edited
		self.currentNote = null;

		//get the next available note ID to assign to a note
		self.getNextId = function() {
			return self.noteIdTracker++;
		};
		//array of notes
		self.notes = ko.observableArray([]);

		//adds a new note to the array of notes with title as the entry inside of the search bar
		self.addNote = function() {
			console.log("'New Note' clicked");
			var title = self.searchBarValue();
			if (title.length > 0) {
				var nextId = self.getNextId();
				console.log("Adding new note " + title + " to list with ID " + nextId);
				self.notes.unshift(new Note(nextId, title, ""));
			} else {
				console.log("Title is blank, not adding note");
			}
		};
		//clear the search bar
		self.clearSearch = function() {
			self.searchBarValue("");
		};
		//delete a note
		self.deleteNote = function(noteToDelete) {
			if (noteToDelete == self.currentNote) {
				self.textAreaValue("");
			}
			self.notes.destroy(noteToDelete);			
		};

		self.updateNote = function(noteToUpdate) {
			noteToUpdate = typeof noteToUpdate !== 'undefined' ? noteToUpdate : self.currentNote;
			if (noteToUpdate != null && self.currentNote.contents() != self.textAreaValue()) {
				self.currentNote.contents(self.textAreaValue());
				self.currentNote.modified(GetDate());
			}
		};
		//select a note
		self.selectNote = function(noteToSelect) {
			self.updateNote();
			self.textAreaValue(noteToSelect.contents());
			self.currentNote = noteToSelect;
		};
	}

	return {
		init: function() {
			var vm = new NoteViewModel();
			ko.applyBindings(vm);
			//initialize list of notes
			$.getJSON('/initdata', function(initData) {
				var koData = $.map(initData, function(note) {
					var koNote = new Note(note.id, note.title, note.contents);
					koNote.modified(Date(note.modified));
					return koNote;
				});
				vm.notes(koData);
			});	
		}
	};
});