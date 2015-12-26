# this program reads a file key.txt and uses it as a "one-time pad" to encrypt msg.txt
# into an equal length file encrypted_msg.txt that can then be decrypted with a knowledge of
# a one-time pad system (modulo 26, no punctuations, just characters, case doesn't matter)
# and the key

#functions

#function to make a list of numbers representing each letter in the input, disregards everything
#not a letter
#0 is a, 1 is b, etc.
def numberize(data):
    letters = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                'q','r','s','t','u','v','w','x','y','z' ];
    Letters = uppercase(letters);

    output = [];

    for li in data:
        for chaar in li:
            for idx, le in enumerate(letters):
                if (chaar == le or chaar == Letters[idx]):
                    output.append(idx); #from 0 to 25

    return output;
#end function

#denumberize
def denumberize(data):
    letters = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                'q','r','s','t','u','v','w','x','y','z' ];
    
    output = [];

    for i in data:
        output.append(letters[i]);

    return output;
#end function

#function to make every character of a string in a list uppercase
def uppercase(data):
    upped = [];
    for li in data:
        upped.append(li.upper());
    return upped;
#end function

oneTimePad = open('key.txt','r');
message = open('msg.txt','r');

key = oneTimePad.readlines(); #reads in each line, stores in a list appended with \n
msg = message.readlines();

keyNumbers = numberize(key);
msgNumbers = numberize(msg);

#use the modulo arithmetic to make our coded message
msgEncryptNum = [];

keyLen = len(keyNumbers);
for i, msg_i in enumerate(msgNumbers):
      #sum modulo, so it's from 0 to 25
    s = (msg_i+keyNumbers[i%keyLen])%26;
    msgEncryptNum.append(s);

msgEncrypt = denumberize(msgEncryptNum);

#write encrypted message
file = open('encrypted_msg.txt','w');
for i,li in enumerate(msgEncrypt):
    file.write(li);

file.close();
