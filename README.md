# **Human-Centered-Security**

Prototypes to test a new form of authentication called TapPassword.
## Running the Prototypes:

In-order to run the prototypes use the following commands:

Tap Password Prototype Command - 
*python tap_password_proto.py*

Tap Password Prototype with Visual Cues Command - 
*python visual_cue_proto.py*

PIN Prototype Command - 
*python pin_proto.py*

## Explanations:

### PIN Prototype - pin_proto.py

An instance of the PINRetriever can be used to gather data for evaluation of PINs. There are 3 main methods that are used to gather data.

create_pin()

- Method used to create a pin.

confirm_pin()

- Method used to confirm the pin.

testing_pins()

- Method used to test the passwords.

### Tap Password Prototype - tap_password_proto.py

An instance of the tap_password_proto.py can be used to gather data for evaluation of TapPasswords. There are 3 main methods that are used to gather data.

create_password()

- Method used to create a TapPassword.

confirm_password()

- Method used to confirm the TapPasswords.

testing_passwords()

- Method used to test the TapPassword.

### Tap Password (Visual Cue) - visual_cue_proto.py

An instance of the PasswordRetriever can be used to gather data for evaluation of TapPasswords with Visual cues. This has two methods that are used to create, confirm and test the passwords.

create_tap_passwords()

- Method used to create and confirm a TapPassword.

test_tap_passwords()

- Method used to test the TapPassword.

### Saving data

- On the first run of a retriever a csv file will be created and on every subsequent run the data will get appended to the same file created earlier.
- After running each retriever a csv file will be created that will contain all the data gathered.


