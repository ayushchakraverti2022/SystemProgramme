import java.io.IOException;

class start{
    public static void main(String[] args) {
        try {
            Runtime.getRuntime().exec("python security.py");
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}