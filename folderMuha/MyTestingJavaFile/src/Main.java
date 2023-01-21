import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;

public class Main {
    public static void main(String[] args) {
        String result;
        String text;
        int counter, randomValue;
        try {
            FileReader fl = new FileReader("1.txt");
            BufferedReader in = new BufferedReader(file);
            String str;
            while ((str = in.readLine()) != null) {
                text = str;
                if (counter == randomValue) {
                    result = text;
                }
                counter++;
            }
            in.close();
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }

    }
}