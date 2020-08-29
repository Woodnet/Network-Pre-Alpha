var auto_refresh = setInterval(
        function ()
        {
          $('#content1').load('changeindex.html');
        }, 1000);
function CopyFunction() {
          var copyText = document.getElementById("encryptionkey");
          copyText.select();
          copyText.setSelectionRange(0, 99999); 
          document.execCommand("copy");
          alert("Copied the Chatserver-Encryption Key!");
} 
function CopyFunction2() {
  var copyText = document.getElementById("encryptionkey2");
  copyText.select();
  copyText.setSelectionRange(0, 99999); 
  document.execCommand("copy");
  alert("Copied the Sec-Network-Encryption Key!");
} 
