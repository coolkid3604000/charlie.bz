#!/opt/rubies/2.1.2/bin/ruby

print "Content-Type: text/html\r\n\r\n"

if ENV["HTTP_USER_AGENT"] =~ /Windows 95/ || ENV["QUERY_STRING"] == "win95" # lmao
  puts <<-HTML
    <TITLE>Charlie Somerville</TITLE>
    <BODY BGCOLOR=#FFD700>
    <H1>Charlie's Home Page</H1>
    <P>
      Welcome to Charlie's Home Page on the World Wide Web.
    <P>
      <IMG SRC=CONSTR~1.GIF WIDTH=38 HEIGHT=38>
    <P>
      <A HREF=mailto:webmaster@charlie.bz>webmaster@charlie.bz</A>
  HTML
  exit
end

puts <<-HTML
<!DOCTYPE html>
<html>
<head>
<title>Charlie Somerville</title>
<style>
body {
  background-color:#000000;
}
canvas {
  display:block;
  width:640px;
  height:480px;
  position:absolute;
  left:50%;
  top:50%;
  margin-left:-320px;
  margin-top:-240px;
  image-rendering: optimizeSpeed;
  image-rendering: -moz-crisp-edges;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: optimize-contrast;
  -ms-interpolation-mode: nearest-neighbor;
}
#nowebsocket {
  width:640px;
  position:absolute;
  left:50%;
  top:50%;
  margin-left:-320px;
  margin-top:-48px;
  color:#ffffff;
  font-family:Arial;
  font-size:18px;
  text-align:center;
}
</style>
</head>
<body>
HTML

if File.read("/proc/loadavg").split.first.to_f > 3
  puts <<-HTML
    <div style="background:#333;color:#ccc;text-align:center;font-family:sans-serif;padding:8px;">
      This site is currently under heavy load, and is slower than usual as a result. Sorry about that.
    </div>
  HTML
end

vnc_path = ENV["QUERY_STRING"] == "hellyeahrealmode" ? "ws-bin/vnc-hellyeahrealmode" : "ws-bin/vnc"

puts <<-HTML
  <div id="nowebsocket">
    <p>Welcome to Charlie's site!</p>
    <p>Please use a browser with WebSockets for the full modern experience.</p>
  </div>
  <canvas id="console"></div>
</body>
<script src='assets/novnc.js?2'></script>
<script>
if("WebSocket" in window) {
  var noWebSocketMessage = document.getElementById("nowebsocket");
  noWebSocketMessage.parentNode.removeChild(noWebSocketMessage);
  var con = document.getElementById("console");
  var rfb = new RFB({ target: con });
  rfb.connect("charlie.bz", 443, null, "#{vnc_path}");
}
</script>
</html>
HTML
