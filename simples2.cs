using UnityEngine;

public class desafiostriangulos : MonoBehaviour
{
    public int lado_1 = 0;
    public int lado_2 = 0;
    public int lado_3 = 0;


    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        if (lado_1 == lado_2 && lado_3 == lado_1)
        {
            Debug.Log("isso é um Equilátero");
        }
        else if (lado_1 == lado_2 || lado_1 == lado_3 || lado_2 == lado_3)
        {
            
            Debug.Log("isso é um Isósceles");
        }
        else
        {
            Debug.Log("isso é um escaleno");

        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
