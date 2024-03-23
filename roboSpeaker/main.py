import os

if __name__ == '__main__':
    print("Welcome to RoB0 speaker - created by Arka")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            os.system(f"PowerShell -Command \"Add-Type -AssemblyName System.speech; $synthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $synthesizer.Speak('{"BYE BYE FRIEND"}');\"")
            break
        command = f"PowerShell -Command \"Add-Type -AssemblyName System.speech; $synthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $synthesizer.Speak('{x}');\""
        os.system(command)
