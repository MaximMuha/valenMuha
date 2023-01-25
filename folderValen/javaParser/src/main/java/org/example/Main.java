package org.example;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Objects;

public class Main {
    public static void main(String[] args) throws IOException {
        ArrayList<String[]> ansque = new ArrayList<>();

        File input = new File("src/main/resources/i0.html");
        var document = Jsoup.parse(input, "UTF-8");
        Elements blocks = document.getElementsByClass("multichoice");
        for (Element block : blocks) {
            String question_result = Objects.requireNonNull(block.select("div.grade").first()).text();
            if (question_result.equals("Баллов: 1,00 из 1,00")) {
                String [] table = new String[2];
                table[0] = Objects.requireNonNull(block.select("div.qtext").first()).text();
                Element answer_div = block.select("div.answer").first();
                table[1] = Objects.requireNonNull(Objects.requireNonNull(Objects.requireNonNull(answer_div).select("[checked=checked]").first()).nextElementSibling()).text().toUpperCase();
                ansque.add(table);
            }
        }
        for (String[] el: ansque) {
            System.out.println(el[0]+"\n"+el[1]+"\n");
            System.out.println();

        }
    }
}