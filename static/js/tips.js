$(() => {
    setInterval( () => {
        $.getJSON("/api" ,function(result) {
            let num = randomIntFromRange(1, result["tips"].length);
            let txt = result["tips"][num]["tip"];
            add_tip(txt, num);
        });
    }, 20000)
});
  // Add a new tip with given text to DOM.
function add_tip(txt, num) {
  $.fn.cornerpopup({
  variant: 9,
  slide: 1,
  timeOut: 15000,
  delay: 500,
  button3: "save",
  colors: "#1821e0",
  bgColor: "#ffffff",
  stickToBottom: 1,
  header: `tip #${num}:`,
  text2: `${txt} &#x1F642;`,
  onBtnClick: () => {
      $.post("/tips", {num: num}, function(res) {
          alert(res);
      });
    }
  });
}