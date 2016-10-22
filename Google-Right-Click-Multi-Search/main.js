var noTextError = new Error('You must highlight a text in order to search!'); 

var searchGoogle = function(word){
    var query = word.selectionText;
    if (query != undefined){chrome.tabs.create({url: "https://www.google.com/search?q=" + query});}
    else{alert('You must highlight a text in order to search!');}
};

var searchGoogleImages = function(word){
    var query = word.selectionText;
    if (query != undefined){chrome.tabs.create({url: "https://www.google.com/search?site=&tbm=isch&q=" + query});}
    else{alert('You must highlight a text in order to search!');}};

var searchGoogleVideos = function(word){
    var query = word.selectionText;
    if (query != undefined){chrome.tabs.create({url: "https://www.google.com/search?site=&tbm=vid&q=" + query});}
    else{alert('You must highlight a text in order to search!');}};

var searchGoogleNews = function(word){
    var query = word.selectionText;
    if (query != undefined){chrome.tabs.create({url: "https://www.google.com/search?site=&tbm=nws&q=" + query});}
    else{alert('You must highlight a text in order to search!');}};

var searchGoogleShopping = function(word){
    var query = word.selectionText;
    if (query != undefined){chrome.tabs.create({url: "https://www.google.com/search?site=&tbm=shop&q=" + query});}
    else{alert('You must highlight a text in order to search!');}};

var searchGoogleMaps = function(word){
    var query = word.selectionText;
    if (query != undefined){chrome.tabs.create({url: "https://www.google.com/maps?q=" + query});}
    else{alert('You must highlight a text in order to search!');}};

var searchGoogleBooks = function(word){
    var query = word.selectionText;
    if (query != undefined){chrome.tabs.create({url: "https://www.google.com/search?site=&tbm=bks&q=" + query});}
    else{alert('You must highlight a text in order to search!');}};

chrome.runtime.onInstalled.addListener
(
    function() 
    {

        chrome.contextMenus.create({
            "title": "Google Overall search",
            "contexts": ["all"],
            "onclick": searchGoogle
        });

        chrome.contextMenus.create({
            "title": "Google Image search",
            "contexts": ["all"],
            "onclick": searchGoogleImages
        });

        chrome.contextMenus.create({
            "title": "Google Video search",
            "contexts": ["all"],
            "onclick": searchGoogleVideos
        });

        chrome.contextMenus.create({
            "title": "Google News search",
            "contexts": ["all"],
            "onclick": searchGoogleNews
        });

        chrome.contextMenus.create({
            "title": "Google Shopping search",
            "contexts": ["all"],
            "onclick": searchGoogleShopping
        });

        chrome.contextMenus.create({
            "title": "Google Maps search",
            "contexts": ["all"],
            "onclick": searchGoogleMaps
        });

        chrome.contextMenus.create({
            "title": "Google Books search",
            "contexts": ["all"],
            "onclick": searchGoogleBooks
        });

 });


