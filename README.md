This repository is the source for https://online-dropchess-stockfish.onrender.com . It is bughouse analysis board, pychess crazyhouse analysisboard downloaded, and 'crazyhouse' replaced with 'bughouse' everywhere. Licenced under AGPL by gbtami, and the used libraries and tools under their own licences. 

# How to host it offline, or somewhere else

Since it uses WASM, to host it you will need custom HTTP headers. Otherwise the site is fully static. One way to host it offline is to download the repository, and run index.js with node.js or run_python with python. It won't work just double-clicking the analysis.html file.
