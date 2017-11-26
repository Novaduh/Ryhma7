var count = context.get('Kys')||0;
count += 1;
context.set('Kys',count);
msg.count = count +"count tallentaa";
msg.payload = count;

return msg;
