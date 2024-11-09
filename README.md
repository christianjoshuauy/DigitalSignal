# Digital Signal Encoder

This is a Python application that encodes binary data into digital signals using different encoding techniques. The following encoding methods are supported:

- NRZ-L
- NRZ-I
- Bipolar AMI
- Pseudoternary
- Manchester
- Differential Manchester

The application will display the encoded digital signal for each technique using `matplotlib` for visualization.

## Prerequisites

- **Python**: Ensure you have Python 3.6 or higher installed.
- **Matplotlib**: This application uses `matplotlib` for plotting. You can install it via pip.

## Installation

1. Clone the repository or download the script file.
   
   ```bash
   git clone https://github.com/your-username/digital-signal-encoder.git
   cd digital-signal-encoder
    ```

2. Install the required matplotlib package.

    ```bash
    pip install matplotlib
    ```

## Usage

1. Run the program by executing the following command in the terminal:

    ```bash
    python digisig.py
    ```

2. When prompted, enter the initial level configuration:
    - Type y if the initial level is low.
    - Type n if the initial level is high.

3. Enter the binary data to be encoded (e.g., 1011001).

4. The program will display a visual plot for each encoding technique.

## Example

    $ python digital_signal_encoder.py
    Is the initial level low? (y/n): y
    Enter binary data (e.g., 1011001): 1011001

Each encoding technique (NRZ-L, NRZ-I, etc.) will be displayed in a separate plot (Separate tabs). Close one method to open the next method. 