set nocompatible
filetype off

call plug#begin('~/.config/nvim/plugged')

Plug 'arcticicestudio/nord-vim'
Plug 'tpope/vim-fugitive'
Plug 'preservim/nerdtree'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'gko/vim-coloresque'

call plug#end()

colorscheme nord
map <silent> <C-n> :NERDTreeFocus<CR>
:noremap <F4> :set hlsearch! hlsearch?<CR>
map <C-t> :tabnew $HOME/
nnoremap Y Y

set number
set mouse=a
set ruler
set showcmd
set background=dark
highlight ColorColumn ctermbg=lightgrey guibg=lightgrey
set nowrap
set smartcase
set hlsearch
set noerrorbells
set tabstop=4 softtabstop=4
set expandtab
set smartindent

let g:python3_host_prog = expand('~/Miniconda/envs/neovim/bin/python3.7')
