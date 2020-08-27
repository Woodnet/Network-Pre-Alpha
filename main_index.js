var auto_refresh = setInterval(
        function ()
        {
          $('#content1').load('chatindex.html');
        }, 1000);
function CopyFunction() {
          /* Get the text field */
          var copyText = document.getElementById("encryptionkey");
          /* Select the text field */
          copyText.select();
          copyText.setSelectionRange(0, 99999); /*For mobile devices*/

          /* Copy the text inside the text field */
          document.execCommand("copy");

          /* Alert the copied text */
          alert("Copied the Encryption Key!");
} 
