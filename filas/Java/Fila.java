import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Fila {
    public static void main(String[] args){
    
    /*A fila segue a estrutura FIFO(First-In, First-Out)
    Por exemplo, pode ser utilizada em uma fila de cinema onde o primeiro a chegar é o primeiro a ser atendido
    
    Conceitos

    -Head ---> Primeiro elemento da fila
    -Tail ---> Ultimo elemento da fila
    -Enqueue ---> Adicionar um elemento no final da fila
    -Dequeue ---> Remover o primeiro elemento da fila

    Funções
    
    - queue.offer(obj) ---> Adiciona um item na fila
    - queue.peek() ---> Retorna o primeiro item da fila
    - queue.poll() ---> Remove o primeiro item da fila. Se utilizado com o print você imprime e deleta ao mesmo tempo
    - queue.isEmpty() ---> Checa se a fila está vazia
    - queue.size() ---> Length da fila

    */
    
   //exemplo de uso

   Scanner scanner = new Scanner(System.in);

   Queue<String> queue = new LinkedList<String>(); // tem que usar LinkedList porque ela implementa a interface Queue, permitindo operações de fila (FIFO).
        
   System.out.println("Bem-vindo ao cinema🍿!");
        System.out.println("Entre com o nome dos 5 clientes que entraram na fila: ");

        for (int i = 0; i<5 ; i++){
            String name = scanner.nextLine();
            queue.offer(name.toUpperCase());
        }

        System.out.printf("%n");
        System.out.printf("Clientes na fila: %s", queue);

        while (!queue.isEmpty()){
            System.out.printf("%nPróximo cliente da fila a ser chamado: %s%n",queue.peek());
            System.out.printf("Cliente %s, pode entrar no cinema!%n", queue.poll());
            System.out.printf("Clientes na fila = %d: %s%n", queue.size(), queue);
            System.out.printf("%n");
        }
        
        scanner.close();
    }
}