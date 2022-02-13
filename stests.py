import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
    
    <head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>ADRESAR LOKACIJA</title>
	<style type="text/css">
	 body{margin: 0px;background-image:url('back.jpg');}
	 header{padding: 10px;text-align: center;background-color:#ffffaa;
	 }	
	 div{background-color: #000000;color: #ffffff;width:30%;height:40%;margin:auto;padding:50px;margin-top:5%;}
     
	</style>
</head>
<body>
<header>ADRESAR LOKACIJA</header>
<main>
 <div><input type=text><label>POSTANSKI BROJ</label><input type="radio" value="true"><label>RAMPA</label><input type="radio" value="false">
 </div>
 <div>
  <a>RAMPA</a><a>35</a><br>	
  <a>MESTO</a><a>Ralja</a><br>	
  <a>GRAD/OPSTINA</a><a>Smederevo</a><br>	
  <a>OKRUG</a><a>Podunavski okrug</a><br>	
 </div>
 <table>
  <tr><td>11050</td><td>33</td><td>Medakovi</td><td>11050</td>
 </table>
</main>
</body>
    """,
    height=100%,
)

