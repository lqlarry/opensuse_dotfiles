let mapleader = " " " map leader to Space
let mapleader = "," " map leader to comma

set ruler
set relativenumber
set hlsearch
set showcmd
set t_Co=ALL

map <leader>h :noh<CR>
map <C-n> :Lexplore<CR>
map <C-t> :tabnew $HOME/
"map <C-v> Cv<CR>
" map <F5> :source ~/.vimrc<CR>
" Press <F4> to toggle highlighting on/off, and show current value.
:noremap <F4> :set hlsearch! hlsearch?<CR>

color adam 
syntax on

let g:netrw_banner = 0
let g:netrw_liststyle = 3
let g:netrw_browse_split = 4
let g:netrw_altv = 1
let g:netrw_winsize = 25

