import java.util.Scanner;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.net.InetAddress;
import java.security.Key;
import java.util.Base64;
import java.io.IOException;


public class CCEncryptService {
    private static final String CUSTOM_KEY = "ClamCorpSecretKeyF0rEncService99";
    private static final byte[] KEY = CUSTOM_KEY.getBytes(StandardCharsets.UTF_8); // 16-byte key for AES-128 encryption
    private static final String ALGORITHM = "AES";
    private static final String TRANSFORMATION = "AES";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Do you want to use the (E)ncryption or (D)ecryption service? ");
        String choice = scanner.nextLine().trim().toUpperCase();

        CCEncryptService.canReachInternalNetwork();

        if (!choice.equals("E") && !choice.equals("D")) {
            System.out.println("Invalid choice. Please choose E for encryption or D for decryption.");
            scanner.close();
            return;
        }

        System.out.print("Enter the string to be processed: ");
        String inputString = scanner.nextLine();
        scanner.close();

        try {
            if (choice.equals("E")) {
                String encryptedString = encrypt(inputString);
                System.out.println("Encrypted string (in Base64 form): " + encryptedString);
            } else {
                String decryptedString = decrypt(inputString);
                System.out.println("Decrypted string: " + decryptedString);
            }
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    public static String encrypt(String value) throws Exception {
        Key key = new SecretKeySpec(KEY, ALGORITHM);
        Cipher cipher = Cipher.getInstance(TRANSFORMATION);
        cipher.init(Cipher.ENCRYPT_MODE, key);

        byte[] encryptedValue = cipher.doFinal(value.getBytes(StandardCharsets.UTF_8));
        return Base64.getEncoder().encodeToString(encryptedValue);
    }

    public static String decrypt(String encryptedValue) throws Exception {
        Key key = new SecretKeySpec(KEY, ALGORITHM);
        Cipher cipher = Cipher.getInstance(TRANSFORMATION);
        cipher.init(Cipher.DECRYPT_MODE, key);

        byte[] decodedValue = Base64.getDecoder().decode(encryptedValue);
        byte[] decryptedValue = cipher.doFinal(decodedValue);
        return new String(decryptedValue, StandardCharsets.UTF_8);
    }

    public static boolean canReachInternalNetwork() {
        String ipAddress = "encryption-service.internal.clam-corp.com";
        int timeout = 5000;

        System.out.println("Attempting to reach internal encryption service...");

        try {
            boolean isReachable = InetAddress.getByName(ipAddress).isReachable(timeout);

            if (isReachable) {
                System.out.println("Able to contact encryption service!");
                return true;
            } else {
                System.out.println("Encryption service is unreachable.");
                System.exit(255);
                return true;
            }
        } catch (IOException e) {
            System.err.println("Error when attempting to contact encryption service.");
            System.exit(254);
        }
        return false;
    }
}
