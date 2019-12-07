function getgames(){
  x = $.get("/currentgames")
  document.write(x.responseText)
}
