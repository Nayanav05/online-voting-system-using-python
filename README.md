# online-voting-system-using-python
Online Voting System based on python gui 
# Online Voting System

This project is a simple **Online Voting System** built using Python's Tkinter library for the GUI. It allows users to validate their voter ID, vote for one of two nominees, and display the voting results. The system tracks which users have already voted to prevent multiple votes from the same user.

## Features

- **Voter ID Validation**: Users can enter their Voter ID and the system checks if the ID is valid.
- **Vote Casting**: After validating the Voter ID, users can cast their vote for one of two nominees.
- **Prevention of Multiple Voting**: The system tracks which Voter IDs have already been used and prevents users from voting more than once.
- **Results Display**: Admins can enter a password to view the results, which displays the winner along with the percentage of votes received.
- **Image and PDF Linking**: Buttons allow the opening of images and PDFs related to the voting system, and a college website.


### Dependencies

- Python 3.x
- Tkinter (standard with Python installation)
- `webbrowser` (standard with Python installation)

### How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/online_voting_system.git
    cd online_voting_system
    ```

2. Ensure you have Python installed (version 3.x).
   
3. Run the script using Python:

    ```bash
    python main.py
    ```

4. The GUI will open, allowing you to interact with the system.

### Usage

1. **Voter ID Entry**:
   - Enter your Voter ID in the input field and click the "Voter ID" button.
   - If your ID is valid, you'll be able to cast a vote.
   - If your ID is invalid or you have already voted, you will receive an error message.

2. **Voting**:
   - After a valid Voter ID, click on one of the nominee buttons to cast your vote.
   - The system will disable the voting buttons after you have voted.

3. **Viewing Results**:
   - Admins can enter the password (default: `2022`) into the password field and click the "Result" button.
   - The system will display the winner and the percentage of votes received by each nominee.

### Customization

- You can add more Voter IDs by editing the `voter_id` list in the code.
- The admin password can be changed by modifying the `password` list in the code.

### Screenshots

#### Main Voting Screen


#### Results Screen


### Contributions

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- This project was developed under the guidance of **Mr. Niranjan Murthy C**, Assistant Professor.
- Special thanks to team members**Asfiya**, **Gagan B S**, and **Gagan P K** for their contributions.



