//imports necessary modules
import java.util.Arrays;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class word_test
{

    //This first function creates an array 'frequency' to store
    //how often each letter appears in the passed array of Strings.
    //Next it creates a new array 'array_2' to be sorted from lowest
    //to highest. This array is then compared to the 'frequency' array
    //to print out the ordered list of the frequency of each letter 
    public static void letter_frequency(String[] words){
        char[] letters = {'a','b','c','d','e','f',
        'g','h','i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z'};
        int[] frequency = new int[letters.length];
        for (int i1 = 0; i1 < letters.length; i1++){
            for (int i2 = 0; i2 < words.length; i2++){
                for (int i3 = 0; i3 < 5; i3++){
                    frequency[i1] += 
                    (words[i2].charAt(i3) == letters[i1]) ? 1 : 0;
                }
            }
        }
        int[] array_2 = new int[frequency.length];
        for (int i4 = 0; i4 < frequency.length; i4++){
            array_2[i4] = frequency[i4];
        }
        Arrays.sort(array_2);
        for (int i4 = 0; i4 < frequency.length; i4++){
            for (int i5 = 0; i5 < frequency.length; i5++){
                if (frequency[i5] == array_2[i4]) {
                    System.out.print(letters[i5]+": "+frequency[i5]);
                }
            }
            System.out.print("\n");
        }

        //returns the number of Strings in the passed array
        System.out.println(words.length);
    }

    //this function looks through the list of passed Strings, and prints
    //any that contain chars 'a', 'b', 'c', and 'd'.
    public static void valid_words(String[] words, char a, char b, char c, char d){
        boolean valid_word = true;
        for (int i2 = 0; i2 < words.length; i2++){
            valid_word = words[i2].contains(String.valueOf(a)) &&
            words[i2].contains(String.valueOf(b)) &&
            words[i2].contains(String.valueOf(c)) &&
            words[i2].contains(String.valueOf(d));
            if (valid_word) System.out.println(words[i2]);
        }
    }

    public static void main(String[] args){

        //Reads from a list of five letter words using Java File/Scanner
        String[] words = new String[5757];
        try{
            File text = new File("words.txt");
            Scanner list_reader = new Scanner(text);
            int words_counter = 0;
            while (list_reader.hasNextLine()){
                words[words_counter] = list_reader.nextLine();
                words_counter++;
            }
            list_reader.close();
        }
        catch (FileNotFoundException e){
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        //Calls both of the above functions
        letter_frequency(words);
        valid_words(words, 's', 't', 'a', 'r');

    }
}