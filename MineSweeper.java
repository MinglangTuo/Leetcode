class mineSweeper{
   


    public static void main(String args[]){
        char[][] abc = {{'E', 'E', 'E', 'E', 'E'},
        {'E', 'E', 'M', 'E', 'E'},
        {'E', 'E', 'E', 'E', 'E'},
        {'E', 'E', 'E', 'E', 'E'}};
       
        int[] click1 = {3,0};
        int[] click2 = {1,2};

        abc = updateBoard(abc, click1);
        abc = updateBoard(abc,click2);

        System.out.println(abc);
    }

    static public char[][] updateBoard(char[][] board, int[] click){
        return visit(board,click[0],click[1]);

    }

    static public char[][] visit(char[][] board, int x,int y){
        if(board[x][y] == 'M'){
            board[x][y] = 'X';
            System.out.println("Game is over!");
            return board;
        }

        int count = 0;

        for(int i = x-1;i<=x+1;i++){
            for(int j = y-1;j<=y+1;j++){
                if(i>=0&&i<board.length&&j>=0&&j<board[0].length){
                if(board[i][j]=='M'){
                    count++;
                }
            }
            }
        }

        if(count !=0){
            board[x][y] = (char)(count+'0');
            return board;
        }
        else{
            board[x][y] = 'B';
            for(int i = x-1;i<=x+1;i++){
                for(int j = y-1;j<=y+1;j++){
                if(i>=0&&i<board.length&&j>=0&&j<board[0].length){
                if(board[i][j] == 'E'){
                    visit(board,i,j);
                }
            }
            }


        }

        return board;
    }




}
}