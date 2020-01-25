import java.io.*;
import java.util.Random;

/*
    hasRunnyNose
    hasHeadache
    hasCough
    hasSoreThroat
    hasFever
    feelsUnwell

    isBleeding
    hasDiscolorations
    isShortOfBreath
    bodyAches
    isFatigued
    isVomiting
    hasDiarrhea
    isNauseous
    hasWateryRedEyes
    hasChills
    noAppetite
    isDizzy
    hasSwellingLimbs
    hasSwellingEyes
    hasSwellingThroat
    hasAbdominalPain
    hasProblemsBalancing
    hasStomachCramps
    hasMemoryLoss
    hasIrritatedThroat
    hasMuscleCramps
    hasItchyEyes
    isInExtremePain
    hasPus
    isBleedingClearLiquid

    hasVirus
 */
public class MakeTests {
    public static void main(String[] args) throws IOException{
        String fileString = "";
        int hasVirus = 0;
        for (int j = 0 ; j < 2000 ; j++) {
            Random random = new Random();
            for (int i = 0; i < 6; i++) { // For the virus symptoms
                boolean randBool = random.nextBoolean();
                if (randBool) {
                    hasVirus += 8;
                } else {
                    hasVirus -= 1;
                }
                fileString = fileString.concat(String.valueOf(randBool) + ",");
            }
            for (int i = 0; i < 24; i++) {
                boolean randBool = random.nextBoolean();
                if (randBool) {
                    hasVirus -= 1;
                } else {
                    hasVirus += 1;
                }
                fileString = fileString.concat(String.valueOf(randBool) + ",");
            }
            boolean randBool = random.nextBoolean();
            if (randBool) {
                hasVirus -= 1;
            } else {
                hasVirus += 1;
            }
            fileString = fileString.concat(String.valueOf(randBool) + "\n");
        }
//        System.out.println(fileString);

        try (PrintWriter writer = new PrintWriter(new File("Test.csv"))) {
            writer.write(fileString);
            writer.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

    }


}
