# Alfred BscScan Search

Alfred workflow to quickly search addresses, transactions, and ENS Domains on BscScan

- [Alfred BscScan Search](#alfred-bscscan-search)
  - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)


## Installation

1. Download the `.alfredworkflow` file from the
[GitHub releases](https://github.com/muyinliu/alfred-bscscan-search/releases/latest) page
2. Double-click the file to install

## Usage

The default keyword is `bs`, but this can be changed if desired. Examples usage:

| Command                | Description                                                                                                         |
|------------------------|---------------------------------------------------------------------------------------------------------------------|
| `bs <address>`         | Opens the provided address on BscScan.                                                                              |
| `bs <transactionHash>` | Opens the provided transaction hash on BscScan.                                                                     |
| `bs <tokenName>`       | Opens the provided token on BscScan. Supported<br>values for `tokenName` include `dai`, `usdc`, `usdt` or `tether`. |

## License

This workflow is released under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgements

This project utilizes the
[alfred-workflow](https://github.com/deanishe/alfred-workflow)
tool built by [@deanishe](https://github.com/deanishe)
