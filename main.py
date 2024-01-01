from __future__ import annotations
import gradio as gr
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def main():
    with gr.Blocks(theme=gr.themes.Glass(neutral_hue="red")) as demo:
        with gr.Row("Select Encryption or decryption") :
            with gr.Column("Encryption"):
                text_input1 = gr.Textbox(label="PLAIN TEXT")
                text_input2 = gr.Textbox(label="KEY")
                text_button1 = gr.Button("ENCRYPT")
                text_output1 = gr.Textbox(label="ENCRYPTED MESSAGE")

            with gr.Column("Decryption"):
                text_input3 = gr.Textbox(label="CIPHER TEXT")
                text_input4 = gr.Textbox(label="KEY")
                text_button2 = gr.Button("DECRYPT")
                text_output2 = gr.Textbox(label="DECRYPTED MESSAGE")


        text_button1.click(autoEncryption, inputs=[text_input1,text_input2], outputs=text_output1)
        text_button2.click(autoDecryption, inputs=[text_input3,text_input4], outputs=text_output2)

    demo.launch()


def autoEncryption(msg, key):
    msg = msg.upper()
    key = key.upper()
    if msg == "" or key == "":
        raise gr.Error("enter the inputs!!!")
    len_msg = len(msg)
    # generating the keystream
    newKey = key + msg
    newKey = newKey[:len(newKey) - len(key)]
    encryptMsg = ""
    # applying encryption algorithm
    for x in range(len_msg):
        first = alphabet.index(msg[x])
        second = alphabet.index(newKey[x])
        total = (first + second) % 26
        encryptMsg += alphabet[total]
    return encryptMsg

def autoDecryption(msg, key):
    msg = msg.upper()
    key = key.upper()
    if msg == "" or key == "":
        raise gr.Error("enter the inputs!!!")
    currentKey = key
    decryptMsg = ""
    # applying decryption algorithm
    for x in range(len(msg)):
        get1 = alphabet.index(msg[x])
        get2 = alphabet.index(currentKey[x])
        total = (get1 - get2) % 26
        total = total + 26 if total < 0 else total
        decryptMsg += alphabet[total]
        currentKey += alphabet[total]
    return decryptMsg.lower()

if __name__ == "__main__":
    main()


