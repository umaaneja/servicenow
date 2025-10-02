<ReportDefinition name="Users with SP Legacy">
    <Description>List of users where splegacy field is not blank</Description>
    <Type>Identity</Type>
    <Query>
        <Filter>
             <And>
                <!-- splegacy not blank -->
                <Condition property="splegacy" operator="NOTNULL"/>
                <!-- must have Workday -->
                <Condition property="applications.name" operator="EQUALS" value="Workday"/>
                <!-- must have Active Directory -->
                <Condition property="applications.name" operator="EQUALS" value="Active Directory"/>
                <!-- must have Azure -->
                <Condition property="applications.name" operator="EQUALS" value="Azure"/>
            </And>
            
        </Filter>
    </Query>
    <Columns>
        <Column property="name" displayName="User Name"/>
        <Column property="displayName" displayName="Display Name"/>
        <Column property="email" displayName="Email"/>
        <Column property="splegacy" displayName="SP Legacy"/>
    </Columns>
</ReportDefinition>
