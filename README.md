This repository is the source for https://online-dropchess-stockfish.onrender.com . It is bughouse analysis board, pychess crazyhouse analysisboard downloaded, and 'crazyhouse' replaced with 'bughouse' everywhere. Licenced under AGPL, and the used libraries and tools under their own licences. 

# How to host it offline, or somewhere else

Since it uses WASM, to host it you will need custom HTTP headers. Otherwise the site is fully static. 

One way to host the site offline is to download the repository, and run run_python with python. Then you can open the site at http://localhost:7878/analysis.html by default.  But any simple file server will work, where you can controll the headers, e.g. apache, node.js, or any static webhosts where you can controll the headers.
