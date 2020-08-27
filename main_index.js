var auto_refresh = setInterval(
        function ()
        {
          $('#content1').load('chatindex.html');
        }, 1000);
function CopyFunction() {
          var copyText = document.getElementById("encryptionkey");
          copyText.select();
          copyText.setSelectionRange(0, 99999); 
          document.execCommand("copy");
          alert("Copied the Encryption Key!");
} 
