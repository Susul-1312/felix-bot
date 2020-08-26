require('dotenv').config();
const fetch = require("node-fetch");
const Discord = require('discord.js');
const client = new Discord.Client();

client.once('ready', () => {
        console.log('Ready!');
});

client.on('message', async function (msg) {

	if (msg.content.toLowerCase() == "-felix")
		var r = await fetch('http://localhost:9000');
		link = await r.text()
		console.log(link)
		msg.channel.send(new Discord.MessageEmbed()
    			.setTitle('<3')
    			.setColor(
      				"#" +
        			(
         				"000000" +
          				Math.random()
            				.toString(16)
            				.slice(2, 8)
            				.toUpperCase()
        			).slice(-6)
    			)
    			.setImage(link))
});

client.login(process.env.TOKEN)
